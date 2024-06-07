# CAE_Custom_Command
Run custom script in Abaqus/CAE with single line of command

# How to use
1. Download the folder and put it in abaqus_v6.env directory <br>
2. The default directory for .env is "C:\SIMULIA\EstProducts\2023\win_b64\SMA\site" (may dependent on version) <br>
3. Edit your abaqus_v6.env file. Copy and paste the line 42 ~ 68 of the attached abaqus_v6.env file <br>
4. Run command in Abaqus python kernel window: <br><br><br>
![image](https://github.com/YB-LIM/CAE_Custom_Command/assets/105615106/9a947397-3847-4b99-bd0a-c24e8a7f9365)

# Command description
**delete_xy()**: Delete all XY-data in Abaqus/viewer <br>
**cantilever()**: Generate a 3D solid cantilever model. No load is applied <br><br>
![image](https://github.com/YB-LIM/CAE_Custom_Command/assets/105615106/ee599849-d661-4309-ba3e-c14585fa15f5) <br>
**block()**: Generate a 3D block model. No BC and load applied <br><br>
![image](https://github.com/YB-LIM/CAE_Custom_Command/assets/105615106/00cfa119-88ba-44c2-b297-9073d79f75f2) <br>


