import h5py
from typing import List, Dict, Union
from pydoc import locate

import numpy as np
import pandas as pd

from tqdm import tqdm

from agora.abc import ParametersABC
from agora.io.writer import Writer
from agora.io.signal import Signal
from agora.io.cells import Cells

from postprocessor.core.processes.merger import mergerParameters, merger
from postprocessor.core.processes.picker import pickerParameters, picker


class PostProcessorParameters(ParametersABC):
    """
    Anthology of parameters used for postprocessing
    :merger:
    :picker: parameters for picker
    :processes: list processes:[objectives], 'processes' are defined in ./processes/
        while objectives are relative or absolute paths to datasets. If relative paths the
        post-processed addresses are used. The order of processes matters.

    """

    def __init__(
        self,
        targets={},
        parameters={},
        outpaths={},
    ):
        self.targets: Dict = targets
        self.parameters: Dict = parameters
        self.outpaths: Dict = outpaths

    def __getitem__(self, item):
        return getattr(self, item)

    @staticmethod
    def find_in_1st(string, lol):
        pass

    @classmethod
    def default(cls, kind=[]):
        targets = {
            "prepost": {
                "merger": "/extraction/general/None/area",
                "picker": ["/extraction/general/None/area"],
            },
            "processes": [
                [
                    "bud_metric",
                    [
                        "/extraction/general/None/volume",
                    ],
                ],
                [
                    "births",
                    [
                        "/extraction/general/None/volume",
                    ],
                ],
                [
                    "dsignal",
                    [
                        "/extraction/general/None/volume",
                        "/postprocessing/bud_metric/extraction_general_None_volume",
                    ],
                ],
                [
                    "aggregate",
                    [
                        [
                            "/extraction/general/None/volume",
                            "postprocessing/bud_metric/extraction_general_None_volume",
                            "postprocessing/dsignal/extraction_general_None_volume",
                            "postprocessing/dsignal/postprocessing_bud_metric_extraction_general_None_volume",
                        ],
                    ],
                ],
            ],
        }
        parameters = {
            "prepost": {
                "merger": mergerParameters.default(),
                "picker": pickerParameters.default(),
            }
        }
        outpaths = {}
        outpaths["aggregate"] = "/postprocessing/experiment_wide/aggregated/"

        if "ph_batman" in kind:
            targets["processes"]["bud_metric"].append(
                [
                    [
                        "/extraction/em_ratio/np_max/mean",
                        "/extraction/em_ratio/np_max/median",
                    ],
                ]
            )
            targets["processes"]["dsignal"].append(
                [
                    "/extraction/em_ratio/np_max/mean",
                    "/extraction/em_ratio/np_max/median",
                    "/extraction/em_ratio_bgsub/np_max/mean",
                    "/extraction/em_ratio_bgsub/np_max/median",
                    "/postprocessing/bud_metric/extraction_em_ratio_np_max_mean",
                    "/postprocessing/bud_metric/extraction_em_ratio_np_max_median",
                ]
            )
            targets["processes"]["aggregate"].append(
                [
                    [
                        "/extraction/em_ratio/np_max/mean",
                        "/extraction/em_ratio/np_max/median",
                        "/extraction/em_ratio_bgsub/np_max/mean",
                        "/extraction/em_ratio_bgsub/np_max/median",
                        "/extraction/gsum/np_max/median",
                        "/extraction/gsum/np_max/mean",
                        "postprocessing/bud_metric/extraction_em_ratio_np_max_mean",
                        "postprocessing/bud_metric/extraction_em_ratio_np_max_median",
                        "postprocessing/dsignal/postprocessing_bud_metric_extraction_em_ratio_np_max_median",
                        "postprocessing/dsignal/postprocessing_bud_metric_extraction_em_ratio_np_max_mean",
                    ]
                ],
            )

        return cls(targets=targets, parameters=parameters, outpaths=outpaths)


class PostProcessor:
    def __init__(self, filename, parameters):
        self.parameters = parameters
        self._filename = filename
        self._signal = Signal(filename)
        self._writer = Writer(filename)

        # self.outpaths = parameters["outpaths"]
        self.merger = merger(
            mergerParameters.from_dict(parameters["parameters"]["prepost"]["merger"])
        )

        self.picker = picker(
            pickerParameters.from_dict(parameters["parameters"]["prepost"]["picker"]),
            cells=Cells.from_source(filename),
        )
        self.classfun = {
            process: self.get_process(process)
            for process, _ in parameters["targets"]["processes"]
        }
        self.parameters_classfun = {
            process: self.get_parameters(process)
            for process, _ in parameters["targets"]["processes"]
        }
        self.targets = parameters["targets"]

    @staticmethod
    def get_process(process):
        """
        Dynamically import a process class from the 'processes' folder.
        Assumes process filename and class name are the same
        """
        return locate("postprocessor.core.processes." + process + "." + process)

    @staticmethod
    def get_parameters(process):
        """
        Dynamically import parameters from the 'processes' folder.
        Assumes parameter is the same name as the file with 'Parameters' added at the end.
        """
        return locate(
            "postprocessor.core.processes." + process + "." + process + "Parameters"
        )

    def run_prepost(self):
        """Important processes run before normal post-processing ones"""

        merge_events = self.merger.run(self._signal[self.targets["prepost"]["merger"]])

        with h5py.File(self._filename, "r") as f:
            prev_idchanges = self._signal.get_merges()

        changes_history = list(prev_idchanges) + [np.array(x) for x in merge_events]
        self._writer.write("modifiers/merges", data=changes_history)

        with h5py.File(self._filename, "a") as f:  # TODO Remove this once done tweaking
            if "modifiers/picks" in f:
                del f["modifiers/picks"]

        indices = self.picker.run(self._signal[self.targets["prepost"]["picker"][0]])

        mothers, daughters = np.array(self.picker.mothers), np.array(
            self.picker.daughters
        )

        multii = pd.MultiIndex.from_arrays(
            (
                np.append(mothers, daughters[:, 1].reshape(-1, 1), axis=1).T
                if daughters.any()
                else [[], [], []]
            ),
            names=["trap", "mother_label", "daughter_label"],
        )
        self._writer.write(
            "postprocessing/lineage",
            data=multii,
            overwrite="overwrite",
        )

        # apply merge to mother-daughter
        moset = set([tuple(x) for x in mothers])
        daset = set([tuple(x) for x in daughters])
        picked_set = set([tuple(x) for x in indices])
        with h5py.File(self._filename, "a") as f:
            merge_events = f["modifiers/merges"][()]
        multii = pd.MultiIndex(
            [[], [], []], [[], [], []], names=["trap", "mother_label", "daughter_label"]
        )
        if merge_events.any():
            merged_moda = set([tuple(x) for x in merge_events[:, 0, :]]).intersection(
                set([*moset, *daset, *picked_set])
            )
            search = lambda a, b: np.where(
                np.in1d(
                    np.ravel_multi_index(a.T, a.max(0) + 1),
                    np.ravel_multi_index(b.T, a.max(0) + 1),
                )
            )

            for target, source in merge_events:
                if (
                    tuple(source) in moset
                ):  # update mother to lowest positive index among the two
                    mother_ids = search(mothers, source)
                    mothers[mother_ids] = (
                        target[0],
                        self.pick_mother(mothers[mother_ids][0][1], target[1]),
                    )
                if tuple(source) in daset:
                    daughters[search(daughters, source)] = target
                if tuple(source) in picked_set:
                    indices[search(indices, source)] = target

            multii = pd.MultiIndex.from_arrays(
                (np.append(mothers, daughters[:, 1].reshape(-1, 1), axis=1).T),
                names=["trap", "mother_label", "daughter_label"],
            )
        self._writer.write(
            "postprocessing/lineage_merged",
            data=multii,
            overwrite="overwrite",
        )

        self._writer.write(
            "modifiers/picks",
            data=pd.MultiIndex.from_arrays(
                indices.T if indices.any() else [[], []],
                names=["trap", "cell_label"],
            ),
            overwrite="overwrite",
        )

    @staticmethod
    def pick_mother(a, b):
        """Update the mother id following this priorities:

        The mother has a lower id
        """
        x = max(a, b)
        if min([a, b]):
            x = [a, b][np.argmin([a, b])]
        return x

    def run(self):
        self.run_prepost()

        for process, datasets in tqdm(self.targets["processes"]):
            if process in self.parameters["parameters"].get(
                "processes", {}
            ):  # If we assigned parameters
                parameters = self.parameters_classfun[process](self.parameters[process])

            else:
                parameters = self.parameters_classfun[process].default()

            loaded_process = self.classfun[process](parameters)
            for dataset in datasets:
                # print("Processing", process, "for", dataset)

                if isinstance(dataset, list):  # multisignal process
                    signal = [self._signal[d] for d in dataset]
                elif isinstance(dataset, str):
                    signal = self._signal[dataset]
                else:
                    raise ("Incorrect dataset")

                if len(signal):
                    result = loaded_process.run(signal)
                else:
                    result = pd.DataFrame(
                        [], columns=signal.columns, index=signal.index
                    )

                if process in self.parameters["outpaths"]:
                    outpath = self.parameters["outpaths"][process]
                elif isinstance(dataset, list):
                    # If no outpath defined, place the result in the minimum common
                    # branch of all signals used
                    prefix = "".join(
                        prefix + c[0]
                        for c in takewhile(
                            lambda x: all(x[0] == y for y in x), zip(*dataset)
                        )
                    )
                    outpath = (
                        prefix
                        + "_".join(  # TODO check that it always finishes in '/'
                            [d[len(prefix) :].replace("/", "_") for d in dataset]
                        )
                    )
                elif isinstance(dataset, str):
                    outpath = dataset[1:].replace("/", "_")
                else:
                    raise ("Outpath not defined", type(dataset))

                if process not in self.parameters["outpaths"]:
                    outpath = "/postprocessing/" + process + "/" + outpath

                if isinstance(result, dict):  # Multiple Signals as output
                    for k, v in result:
                        self.write_result(
                            outpath + f"/{k}",
                            v,
                            metadata={},
                        )
                else:
                    self.write_result(
                        outpath,
                        result,
                        metadata={},
                    )

    def write_result(
        self, path: str, result: Union[List, pd.DataFrame, np.ndarray], metadata: Dict
    ):
        self._writer.write(path, result, meta=metadata)


def _if_dict(item):
    if hasattr(item, "to_dict"):
        item = item.to_dict()
    return item
