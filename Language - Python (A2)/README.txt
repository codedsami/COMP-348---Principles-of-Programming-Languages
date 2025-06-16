TESTED ON UBUNTU

How to Run:
Go to the designated folder and run:
example: cd /mnt/c/Users/Mahmu/OneDrive/Desktop/COMP\ 348\ ASSIGNMENTS/Language\ -\ Python\ \(A2\)/
python3 main.py

If You Get Errors (Missing Libraries)

Install the required packages:

sudo apt update
sudo apt install python3-pip
python3 -m pip install matplotlib

if pip refuses to install due to managed environment:

python3 -m venv venv
source venv/bin/activate
pip install matplotlib
python3 main.py


Once the project runs:
choose option 1(load file) and write-> data.txt