#!/bin/bash

echo "What is github username?"
read username
echo "What is your e-mail connected to $username" 
read e_mail

git config --global user.name "$username"
git config --global user.email "$e_mail"


