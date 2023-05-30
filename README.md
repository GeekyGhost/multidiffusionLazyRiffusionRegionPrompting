# multidiffusionLazyRiffusionRegeionPrompting
Testing script for region prompting in the Automtaic1111 Multidiffusion extension for Riffusion usage

This creates a json file for multidiffusion to load settings. It either makes them all the same prompt or it alternates between two prompt. 
It fills in all 8 boxes with settings designs for a 512x4096 Spectrogram using the Riffusion model which can be found on Civitai. 
All settings can be manually changed in the code itself. I may add UI features to do it if theres any inteterest. 
Mainly using it for testing but obviously if testing works out I can kind of add to it to make a prompt formatter for different types of genres or who knows. 

Enter one or two prompts, choose the feathering amount. Enter the seed. Then enter the variation amount for the seed, basic intervals for now. Previous seed + a set number = new seed. Hit the Variationator button and name and save your json file. Then Viola! you have a template for Multidiffusion for your Riffusion testing of regional prompting. 

I usually use a .bat fule to create the venv and activate it then install requirements and then launch the main.py file but there's really no dependencies here. Pretty basic. Create the venv, activate it, run the script. No requirements lol. 

This is meant to create json files for https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111

![Screenshot 2023-05-30 123232](https://github.com/GeekyGhost/multidiffusionLazyRiffusionRegeionPrompting/assets/111990299/b4417720-3b0b-4011-860d-67ff93eeab91)

![Screenshot 2023-05-30 114832](https://github.com/GeekyGhost/multidiffusionLazyRiffusionRegeionPrompting/assets/111990299/0691f71c-903f-40ff-9769-575f8ad814ee)

![tmpsbpy5ltv](https://github.com/GeekyGhost/multidiffusionLazyRiffusionRegeionPrompting/assets/111990299/d5137ecc-f778-4745-8dad-22c8292f722c)



Code created with the assistance of chatGPT4
