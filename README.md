# multidiffusionLazyRiffusionRegeionPrompting
Testing script for region prompting in the Automtaic1111 Multidiffusion extension for Riffusion usage

This creates a json file for multidiffusion to load settings. It either makes them all the same prompt or it alternates between two prompt. 
It fills in all 8 boxes with settings designs for a 512x4096 Spectrogram using the Riffusion model which can be found on Civitai. 
All settings can be manually changed in the code itself. I may add UI features to do it if theres any inteterest. 
Mainly using it for testing but obviously if testing works out I can kind of add to it to make a prompt formatter for different types of genres or who knows. 

Enter one or two prompts, choose the feathering amount. Enter the seed. Then enter the variation amount for the seed, basic intervals for now. Previous seed + a set number = new seed. Hit the Variationator button and name and save your json file. Then Viola! you have a template for Multidiffusion for your Riffusion testing of regional prompting. 

I usually use a .bat file to create the venv and activate it then install requirements and then launch the main.py file but there's really no dependencies here. Pretty basic. Create the venv, activate it, run the script. No requirements lol. 

This is meant to create json files for https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111

![Screenshot 2023-05-30 123232](https://github.com/GeekyGhost/multidiffusionLazyRiffusionRegeionPrompting/assets/111990299/b4417720-3b0b-4011-860d-67ff93eeab91)

![Screenshot 2023-05-30 143425](https://github.com/GeekyGhost/multidiffusionLazyRiffusionRegionPrompting/assets/111990299/79ccd9fc-ef63-4dd4-8f53-7bad1724dc0e)

![tmpsbpy5ltv](https://github.com/GeekyGhost/multidiffusionLazyRiffusionRegeionPrompting/assets/111990299/d5137ecc-f778-4745-8dad-22c8292f722c)

Example json file output

{
    "bbox_controls": [
        {
            "enable": true,
            "x": 0,
            "y": 0,
            "w": 0.15,
            "h": 1,
            "prompt": "Metal Ballad",
            "neg_prompt": "",
            "blend_mode": "Foreground",
            "feather_ratio": 0.05,
            "seed": 421369420711
        },
        {
            "enable": true,
            "x": 0.15,
            "y": 0,
            "w": 0.1,
            "h": 1,
            "prompt": "Rock Ballad",
            "neg_prompt": "",
            "blend_mode": "Foreground",
            "feather_ratio": 0.05,
            "seed": 421369420839
        },
        {
            "enable": true,
            "x": 0.25,
            "y": 0,
            "w": 0.15,
            "h": 1,
            "prompt": "Metal Ballad",
            "neg_prompt": "",
            "blend_mode": "Foreground",
            "feather_ratio": 0.05,
            "seed": 421369420967
        },
        {
            "enable": true,
            "x": 0.4,
            "y": 0,
            "w": 0.1,
            "h": 1,
            "prompt": "Rock Ballad",
            "neg_prompt": "",
            "blend_mode": "Foreground",
            "feather_ratio": 0.05,
            "seed": 421369421095
        },
        {
            "enable": true,
            "x": 0.5,
            "y": 0,
            "w": 0.15,
            "h": 1,
            "prompt": "Metal Ballad",
            "neg_prompt": "",
            "blend_mode": "Foreground",
            "feather_ratio": 0.05,
            "seed": 421369421223
        },
        {
            "enable": true,
            "x": 0.65,
            "y": 0,
            "w": 0.1,
            "h": 1,
            "prompt": "Rock Ballad",
            "neg_prompt": "",
            "blend_mode": "Foreground",
            "feather_ratio": 0.05,
            "seed": 421369421351
        },
        {
            "enable": true,
            "x": 0.75,
            "y": 0,
            "w": 0.15,
            "h": 1,
            "prompt": "Metal Ballad",
            "neg_prompt": "",
            "blend_mode": "Foreground",
            "feather_ratio": 0.05,
            "seed": 421369421479
        },
        {
            "enable": true,
            "x": 0.9,
            "y": 0,
            "w": 0.1,
            "h": 1,
            "prompt": "Rock Ballad",
            "neg_prompt": "",
            "blend_mode": "Foreground",
            "feather_ratio": 0.05,
            "seed": 421369421607
        }
    ]
}



Code created with the assistance of chatGPT4
