import time
import os
from src.data_types import CallbacksConfig
import tensorflow as tf
import warnings


warnings.filterwarnings('ignore')


class Callbacks:
    def __init__(self, config: CallbacksConfig):
        self.config = config

    @property
    def _tensorboard(self):
        timestamp = time.strftime("%Y-%m-%d-T%H-%M-%S")
        logs_dir = os.path.join(self.config.tensorboard_dir, timestamp)
        return tf.keras.callbacks.TensorBoard(logs_dir)

    @property
    def _checkpoint(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath = self.config.checkpoint_path,
            save_best_only = True
        )

    def get_callbacks(self):
        return [self._tensorboard, self._checkpoint]