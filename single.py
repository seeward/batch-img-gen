import os
import time
import torch
import argparse
from diffusers import DiffusionPipeline

class Predictor:
    def __init__(self):
        self.pipe = self._load_model()

    def _load_model(self):
        model = DiffusionPipeline.from_pretrained("SimianLuo/LCM_Dreamshaper_v7")
        # Load model onto CPU then move to MPS if available.
        model.to(torch_device="cpu", torch_dtype=torch.float32).to('mps:0')
        return model

    def predict(self, prompt: str, width: int, height: int, steps: int, seed: int = None, output_dir: str = None) -> str:
        seed = seed or int.from_bytes(os.urandom(2), "big")
        print(f"Using seed: {seed}")
        torch.manual_seed(seed)

        result = self.pipe(
            prompt=prompt,
            width=width,
            height=height,
            guidance_scale=8.0,
            num_inference_steps=steps,
            num_images_per_prompt=1,
            lcm_origin_steps=50,
            output_type="pil"
        ).images[0]

        return self._save_result(result, output_dir, prompt, seed)
    
    def _save_result(self, result, output_dir: str, prompt: str, seed: int) -> str:
        if output_dir is None:
            output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        # Replace spaces in the prompt to create a safe filename.
        safe_prompt = prompt.replace(" ", "_")
        output_path = os.path.join(output_dir, f"{safe_prompt}-{seed}-{timestamp}.png")
        result.save(output_path)
        return output_path

def main():
    args = parse_args()
    predictor = Predictor()

    batch_folder = "output"
    if not os.path.exists(batch_folder):
        os.makedirs(batch_folder)
    
    for i in range(args.count):
        print(f"Generating image {i+1}/{args.count} with prompt: '{args.prompt}'")
        output_path = predictor.predict(args.prompt, args.width, args.height, args.steps, args.seed, output_dir=batch_folder)
        print(f"Output image saved to: {output_path}")

def parse_args():
    parser = argparse.ArgumentParser(description="Generate images based on a single text prompt, repeated as many times as specified by --count.")
    parser.add_argument("--prompt", type=str, required=True, help="A single text prompt for image generation.")
    parser.add_argument("--width", type=int, default=512, help="The width of the generated image.")
    parser.add_argument("--height", type=int, default=512, help="The height of the generated image.")
    parser.add_argument("--steps", type=int, default=8, help="The number of inference steps.")
    parser.add_argument("--seed", type=int, default=None, help="Seed for random number generation.")
    parser.add_argument("--count", type=int, default=1, help="Number of times to generate the prompt.")
    return parser.parse_args()

if __name__ == "__main__":
    main()
