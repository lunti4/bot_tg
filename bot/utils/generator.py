import replicate

def get_model_url(model: str):
    if model == "SDXL":
        return "stability-ai/sdxl:7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc"
    elif model == "MANGA":
        return "aramintak/bandw-manga:f71e6abfc606137e777d505cbb2d166de45fc5cfcc847a1d07e97af63a03748d"

def generate_pic(input: str, model: str):

    model_url = get_model_url(model)

    if model == "SDXL":
        scheduler = "K_EULER"
    else:
        scheduler = "Default"

    try:
        output = replicate.run(
            f'{model_url}',
            input={
                "width": 768,
                "height": 768,
                "prompt": f'{input}',
                "refine": "expert_ensemble_refiner",
                "scheduler": f'{scheduler}',
                "lora_scale": 0.6,
                "num_outputs": 1,
                "guidance_scale": 7.5,
                "apply_watermark": False,
                "high_noise_frac": 0.8,
                "negative_prompt": "",
                "prompt_strength": 0.8,
                "num_inference_steps": 25
            }
        )
        return output
    except Exception as e:
        return -1
