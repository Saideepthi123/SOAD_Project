import 'dart:convert';

import 'package:flutter/material.dart';

class User extends ChangeNotifier{
  String _username;
  String _email;
  String _firstName;
  String _lastName;
  String _phoneNumber;
  String _token;
  int _uid;

  get uid => _uid;
  get username => _username;
  get email => _email;
  get firstName => _firstName;
  get lastName => _lastName;
  get phoneNumber => _phoneNumber;
  get token => _token;

  populateUserRegister(String data){
      Map json=jsonDecode(data);
      _uid=json["userID"];
      _username=json["username"];
      _email=json["email"];
      _firstName=json["first_name"];
      _lastName=json["last_name"];
      _phoneNumber=json["phone_number"];
      _token=json["token"];
  }

  populateUserLogin(String data){
    Map json=jsonDecode(data);
    _uid=json["userID"];
    _username=json["username"];
    _email=json["email"];
    _firstName=json["first_name"];
    _lastName=json["last_name"];
    _phoneNumber=json["phone_number"];
    _token=json["token"];
  }



}