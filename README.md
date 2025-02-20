# Image Generation Script Usage Instructions

This guide explains how to use the image generation script that leverages a diffusion model to generate images based on a text prompt. The script supports both single image generation and batch mode to produce multiple images with the same prompt.

---

## Prerequisites

- Set up from here: https://replicate.com/blog/run-latent-consistency-model-on-mac

## Command-Line Arguments

The script uses several command-line arguments to control its behavior:

- `--prompt` (required):  
  A single text prompt that describes the image you want to generate.

- `--width`:  
  The width of the generated image in pixels.  
  _Default:_ `512`

- `--height`:  
  The height of the generated image in pixels.  
  _Default:_ `512`

- `--steps`:  
  The number of inference steps for the diffusion process.  
  _Default:_ `8`

- `--seed`:  
  Seed for random number generation. If not provided, a random seed is generated.

- `--count`:  
  The number of times the prompt will be used to generate images in batch mode.  
  _Default:_ `1`

- `--batch`: Make images as many as count

- `--subject`: Generate prompts for this subject in batches

---

## Usage Examples

### 1. Generate batch from a Single Prompt

Run the following command to generate one image using your text prompt:

```bash
python single.py --prompt "A serene mountain landscape" --width 512 --height 512 --steps 4 --count 10
```

### 2. Generate Multiple Images (Batch Mode) Random Prompts

To generate multiple images with the same prompt, specify the `--count` argument:

```bash
python3 batch.py --subject "A futuristic cityscape" --count 5 --width 512 --height 512 --steps 4 --batch
```

This command will generate 5 images with the prompt "A futuristic cityscape", and all images will be saved in the `output` folder.

---

## Output Details

- **Output Directory:**  
  All images from single.py are saved in the `output` directory.  
  If the directory does not exist, it will be created automatically.

- **Filename Format:**  
  Each output image filename includes:
  - A sanitized version of the prompt (spaces replaced with underscores)
  - The seed used for random number generation
  - A timestamp indicating when the image was generated

---

## Troubleshooting

- **Model Access:**  
  Ensure the diffusion model `"SimianLuo/LCM_Dreamshaper_v7"` is available and accessible.

- **Dependency Issues:**  
  If you encounter issues with dependencies, try updating or reinstalling the required packages.

- **Hardware Configuration:**  
  Confirm that your hardware (CPU, MPS, or GPU) is properly set up to run the script.

---

## License

_Include any license information or additional notes here if needed._

---

By following these instructions, you can effectively generate images using your specified prompt, either as a single output or in batch mode. Enjoy exploring creative image generation!
