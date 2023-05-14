# Automatic-Attendance-System
Welcome to the face recognition project! This project is designed to help you build a facial recognition system that can identify individuals from a dataset of facial images.

To get started with this project, please make sure you have the following:

A computer with a webcam.
A Python environment with the necessary dependencies installed. Recommended : default venv to create a new environment for this project.
Once you have the necessary requirements, you can begin by following these steps:

Clone the project repository from Github.
Install the necessary dependencies by running pip install -r libraries-required.txt.
This project makes use of Firebase' real-time database to update the attendance. So firstly build a database and storage on FB server.
Add the unique ids assigned to each student manuall or by using a .csv file to the AddDataToDatabase file. Then add the images of students, named in accordance to this unique id to the images folder.
Then create their encodings by running the EncodeGenerator.py file. Once this is done, simply run the main.py file to acces the webcam or any other device.
We recommend experimenting with different hyperparameters, model architectures, and training techniques to improve the accuracy of your facial recognition system. You can also try using different datasets or incorporating additional features such as age or gender estimation.
Good luck with your project! If you have any questions or issues, please refer to the documentation or open an issue on the Github repository.
