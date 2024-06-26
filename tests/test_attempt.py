# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import contextlib
import json
import os
import pytest

import garak.cli


def test_attempt_sticky_params(capsys):
    garak.cli.main(
        "-m test.Blank -g 1 -p atkgen,dan.Dan_6_0 --report_prefix _garak_test_attempt_sticky_params".split()
    )
    reportlines = (
        open("_garak_test_attempt_sticky_params.report.jsonl", "r", encoding="utf-8")
        .read()
        .split("\n")
    )
    complete_atkgen = json.loads(reportlines[3])  # status 2 for the one atkgen attempt
    complete_dan = json.loads(reportlines[23])  # status 2 for the one dan attempt
    assert complete_atkgen["notes"] != {}
    assert complete_dan["notes"] == {}
    assert complete_atkgen["notes"] != complete_dan["notes"]
