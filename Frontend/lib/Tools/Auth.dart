import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart';

Future<Response> login (String email,String username,String phone,String password,String firstname,){
  return post('http://http://flare191.pythonanywhere.com/api/auth/register/',headers: <String,String>{
    'Content-Type': 'application/json; charset=UTF-8',
  },
  body: jsonEncode(<String,String>{
    "email": email,
    "username": username,
    "password": password,
    "first_name": firstname,
    "last_name": "packurbags",
    "phone_number": phone,
  }));
}