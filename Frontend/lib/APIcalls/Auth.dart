import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart';

class AuthService{
  static final url="https://packurbags.azurewebsites.net/api/";

  static Future<Response> register (String email,String username,String phone,String password,String firstname,){
    return post(url+'auth/register/',headers: <String,String>{
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

  static Future<Response> login (String email, String password){
    return post(url+'auth/login/',headers: <String,String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
      body: jsonEncode(<String, String>{
        "email": email,
        "password": password,
      })
    );
  }



}




