abschlussprojekt

[![Open in VS Code](https://img.shields.io/badge/Open%20in-VS%20Code-blue?logo=visual-studio-code)](https://github.dev/BulliBrick/abschlussprojekt)

*Click the button* to open the VScode repo in the web

After that click on the Icon in the bottom left corner with Github written next to it.

This will open a bunch of possible options.

Navigate to "Continue Working on Local clone" and follow the instructions

Now you should have a loca copy of the project 

To launch it as a devcontainer you just need to click the blue Button in the bottom left corner again and navigate to "Reopen in Container"

Now it will take some time to launch. 

In the meanwhile you can look around the code and you will find the contents of the Project.

In short it contains a Mysql Database with the options to alter the Data with Phpmyadmin or with the ipynb (Jupyter Notebook). 

As soon as your devcontainer has completly started you can either go on phpmyadmin with localhot:8080 or use the ipynb to alter the Data.

If you chose the phpmyadmin route the username and password are "root"

If you instead use the Jupyter Notebook, you have to do one extra step. 
If you press "Run" next to the first code cell it will prompt you with an install request. You can click install and after that it should work.
If it doesnt work make sure you have a python kernel selected and have run the first cell before any other cells. 

*Debug*

To debug the Jupyter Notebook code hover over the arrow next to the cell you want to debug. Click on the more arrow (looks like a v ) and click "Debug cell" otherwise you an click crtl + shift + alt + enter whilst in the cell you want to debug. You can see in which cell you are by the blue outline of the cell.