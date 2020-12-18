

REGISTRY = {}

from .rnn_agent import RNNAgent
from .noise_rnn_agent import RNNAgent as NoiseRNNAgent
from .rnn_v_agent import RNNVAgent
from .maven_rnn_agent import MavenRNNAgent

REGISTRY["rnn"] = RNNAgent
REGISTRY["rnn_v"] = RNNVAgent
REGISTRY["noise_rnn"] = NoiseRNNAgent
REGISTRY["maven_rnn"] = MavenRNNAgent