# CAE_Custom_Command
Run custom script in Abaqus/CAE with single line of command

# How to use
1. Download the folder and put it in abaqus_v6.env directory <br>
2. The default directory for .env is "C:\SIMULIA\EstProducts\2023\win_b64\SMA\site" (may dependent on version) <br>
3. Edit your abaqus_v6.env file. Copy and paste the line 42 ~ 68 of the attached abaqus_v6.env file <br>
![image](https://github.com/YB-LIM/CAE_Custom_Command/assets/105615106/a82c20e5-a449-4563-b389-d7943631e6c4) <br><br>
4. Change script_dir variable in abaqus_v6.env file if necessary <br>
5. Run command in Abaqus python kernel window: <br><br><br>
![image](https://github.com/YB-LIM/CAE_Custom_Command/assets/105615106/9a947397-3847-4b99-bd0a-c24e8a7f9365)

# Command description
**delete_xy()**: Delete all XY-data in Abaqus/viewer <br>
**cantilever()**: Generate a 3D solid cantilever model. No load is applied <br><br>
![image](https://github.com/YB-LIM/CAE_Custom_Command/assets/105615106/ee599849-d661-4309-ba3e-c14585fa15f5) <br><br>
**block()**: Generate a 3D block model. No BC and load applied <br><br>
![image](https://github.com/YB-LIM/CAE_Custom_Command/assets/105615106/00cfa119-88ba-44c2-b297-9073d79f75f2) <br><br>
**beam()**: Generate a 3D beam element model. No load is applied <br><br>
![image](https://github.com/YB-LIM/CAE_Custom_Command/assets/105615106/3e97b1d1-369c-49b1-98b6-cff163354d57) <br><br>
**shell()**: Generate a 3D shell model. No BC and load applied <br><br>
![image](https://github.com/YB-LIM/CAE_Custom_Command/assets/105615106/9b809474-5239-4743-8390-f5f3a7171820) <br><br>
**single_ut()**: Generate a single element model under uniaxial tension <br><br>
![image](https://github.com/YB-LIM/CAE_Custom_Command/assets/105615106/327069e5-7759-48d1-ae18-8fbbca24a2c8) <br><br>
**single_uc**: Generate a single element model under uniaxial compression <br>
**single_ct**: Generate a single element model confined tension <br>
**single_cc**: Generate a single element model confined compression <br>





