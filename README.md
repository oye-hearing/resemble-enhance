# Resemble Enhance

[![PyPI](https://img.shields.io/pypi/v/resemble-enhance.svg)](https://pypi.org/project/resemble-enhance/)
[![Hugging Face Space](https://img.shields.io/badge/Hugging%20Face%20%F0%9F%A4%97-Space-yellow)](https://huggingface.co/spaces/ResembleAI/resemble-enhance)
[![License](https://img.shields.io/github/license/resemble-ai/Resemble-Enhance.svg)](https://github.com/resemble-ai/resemble-enhance/blob/main/LICENSE)
[![Webpage](https://img.shields.io/badge/Webpage-Online-brightgreen)](https://www.resemble.ai/enhance/)

https://github.com/resemble-ai/resemble-enhance/assets/660224/bc3ec943-e795-4646-b119-cce327c810f1

Resemble Enhance is an AI-powered tool that aims to improve the overall quality of speech by performing denoising and enhancement. It consists of two modules: a denoiser, which separates speech from a noisy audio, and an enhancer, which further boosts the perceptual audio quality by restoring audio distortions and extending the audio bandwidth. The two models are trained on high-quality 44.1kHz speech data that guarantees the enhancement of your speech with high quality.

This Github fork of the Resemble Enhance allows the source code to be built as a `wheel` to further include in the Oye 
Hearing `aislar-voz` code and deployment. The reasons to build the wheel are -
1. To overcome incompatible dependencies from the `resemble-enhance` module from PyPi, which requires much older versions of some of the important third party modules such as `torch` and `torchaudio`.
2. To build separate modules for inference and training in order to exclude unnecessary dependencies during 
   inference, that are required only for training. The main dependency in question here is the `deepspeed`Python 
   module, which requires additional CUDA libraries to be built into the OS for NVIDIA GPU based deployments. This 
   library is required by `resemble-enhance` for training only.


> [!NOTE]
> A separate module or wheel named `resemble_enhance_inference` is built for use in the `aislar-voz` and other Oye applications

Another change is to use Python 3.12 as the base version instead of 3.10.

## Build

To build the wheel file:

```bash
> python3.12 -m venv <venvName>
> . .<venvName>/bin/activate
> python -m build
```

After the `wheel` is successfully built, copy the wheel file to the desired Python application location to use in 
that application.

The wheel file will be in the `dist` directory, and the name will be of the format 
`resemble_enhance_inference-<version>-py3-none-any.whl`.

The value of `<version>` will be that from the `pyproject.toml` file. To update the version, update it in that file, 
rebuild the wheel, commit the changes, and then push and merge the branch into the `main` branch.

## Usage

> [!NOTE]
> The `Enhance` and `Denoise` CLI scripts, and the `Web Demo` have not been tested with this forked branch version of 
> `resemble-enhance`. These will likely still work, but cannot be guaranteed. The built wheel has been tested for 
> denoising with `aislar-voz` aka the Oye isolation server.

### Enhance

```
resemble-enhance in_dir out_dir
```

### Denoise only

```
resemble-enhance in_dir out_dir --denoise_only
```

## Blog

Learn more on our [website](https://www.resemble.ai/enhance/)!
