from enum import Enum


class DriverTypeEnum(str, Enum):
    AMD_GPU_FREE = 'amd gpu free'
    AMD_GPU_PRO = 'amd gpu pro'
    NVIDIA_MAXWELL = 'nvidia Maxwell'
    NVIDIA_MAXWELL_DKMS = 'nvidia Maxwell dkms'
    NVIDIA_KEPLER = 'nvidia Kepler'
    NVIDIA_NVCX_AND_NVDX = 'nvidia 400/500/600 series'
    NVIDIA_TESLA = 'nvidia Telsa'


class LoggerStatusEnum(str, Enum):
    INFO = 'Info'
    WARNING = 'Warning'
    ERROR = 'Error'
