###############################################################################
# (c) Copyright 2021 CERN for the benefit of the LHCb Collaboration           #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "COPYING".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################
"""
Contains utility functions used to display and save the output of the checks.
"""
import copy
import json
from os.path import join

import uproot


def hist_to_root(job_name, check_result, output_path):
    """
    Save histograms in a root file.
    """
    # Create the file only if the check produce histograms in output
    checks_with_histo = ["range", "range_nd", "range_bkg_subtracted"]
    if check_result.check_type in checks_with_histo:
        file_name = f"{job_name}_{check_result.check_type}_histograms.root"
        with uproot.recreate(join(output_path, file_name)) as file_root:
            for key, data in check_result.tree_data.items():
                for hist_counter, _histo in enumerate(data.get("histograms", [])):
                    histo_name = f"{key}/{hist_counter-1}"
                    file_root[histo_name] = _histo


def checks_to_JSON(
    checks_data,
    all_check_results,
    json_output_path=None,
):
    """
    Serialise information about all checks into a JSON format
    """
    all_check_results_copy = copy.deepcopy(all_check_results)

    result = {}
    for job in all_check_results_copy:
        result[job] = {}
        for check in all_check_results_copy[job]:
            result[job][check] = {}

            result[job][check]["passed"] = all_check_results_copy[job][check].passed
            result[job][check]["messages"] = all_check_results_copy[job][check].messages
            result[job][check]["input"] = checks_data[check]
            result[job][check]["output"] = all_check_results_copy[job][check].tree_data

            # Temporary: remove histograms until a good way to serialise them is found
            for tree in result[job][check]["output"]:
                if "histograms" in result[job][check]["output"][tree]:
                    hist_placeholder = ["placeholder"] * len(
                        result[job][check]["output"][tree]["histograms"]
                    )
                    result[job][check]["output"][tree]["histograms"] = hist_placeholder

    if json_output_path is not None:
        with open(json_output_path, "w", encoding="utf8") as json_file:
            json.dump(result, json_file, indent="  ")

    return json.dumps(result, indent="  ")
