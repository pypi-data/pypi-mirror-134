#  Copyright (c) 2022 GradsFlow. All rights reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
from typing import Dict, List, Optional

import wandb

from gradsflow.callbacks.base import Callback
from gradsflow.utility.imports import requires

CURRENT_FILE = os.path.dirname(os.path.realpath(__file__))


def define_metrics():
    min_max_def: Dict[str, List[str]] = {
        "min": ["train/step_loss", "train/epoch_loss", "val/epoch_loss"],
        "max": ["train/acc*", "val/acc*"],
    }
    for summary, metric_list in min_max_def.items():
        for metric in metric_list:
            if "epoch" in metric or "val" in metric:
                wandb.define_metric(metric, summary=summary, step_metric="epoch")
    wandb.define_metric("*", step_metric="global_step")


class WandbCallback(Callback):
    """
    [Weights & Biases](https://www.wandb.com/) Logging callback. To use this callback `pip install wandb`.
    Args:
        log_model: Whether to upload model artifact to Wandb
        code_file: path of the code you want to upload as artifact to Wandb
    """

    @requires("wandb", "WandbCallback requires wandb to be installed!")
    def __init__(
        self,
        log_model: bool = False,
        code_file: Optional[str] = None,
    ):
        super().__init__()
        if wandb.run is None:
            raise ValueError("You must call wandb.init() before WandbCallback()")
        self._code_file = code_file
        self._train_prefix = "train"
        self._val_prefix = "val"
        self._log_model = log_model
        self._setup()

    def _setup(self):
        define_metrics()

    def on_fit_start(self):
        if self._log_model:
            wandb.log_artifact(self.model.learner)
        if self._code_file:
            wandb.log_artifact(self._code_file)

    def _apply_prefix(self, data: dict, prefix: str):
        data = {f"{prefix}/{k}": v for k, v in data.items()}
        return data

    def on_train_step_end(self, outputs: dict = None, **_):
        # self._step(prefix=self._train_prefix, outputs=outputs)
        prefix = "train"
        global_step = self.model.tracker.global_step
        loss = outputs["loss"].item()
        # log train step loss
        wandb.log({f"{prefix}/step_loss": loss, "train_step": global_step}, commit=False)

        # log train step metrics
        metrics = outputs.get("metrics", {})
        metrics = self._apply_prefix(metrics, prefix)
        wandb.log(metrics, commit=False)

        # https://docs.wandb.ai/guides/track/log#how-do-i-use-custom-x-axes
        wandb.log({"global_step": global_step})

    def on_epoch_end(self):
        epoch = self.model.tracker.current_epoch
        train_loss = self.model.tracker.train_loss
        train_metrics = self.model.tracker.train_metrics.to_dict()
        val_loss = self.model.tracker.val_loss
        val_metrics = self.model.tracker.val_metrics.to_dict()

        train_metrics = self._apply_prefix(train_metrics, prefix=self._train_prefix)
        val_metrics = self._apply_prefix(val_metrics, prefix=self._val_prefix)
        train_metrics.update({"epoch": epoch})
        val_metrics.update({"epoch": epoch})

        wandb.log({"train/epoch_loss": train_loss, "epoch": epoch}, commit=False)
        wandb.log({"val/epoch_loss": val_loss, "epoch": epoch}, commit=False)
        wandb.log(train_metrics, commit=False)
        wandb.log(val_metrics, commit=False)
        wandb.log({})
