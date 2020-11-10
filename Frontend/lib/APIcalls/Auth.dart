import 'dart:convert';
import 'dart:io';
import 'dart:html' as http;
import 'package:http/http.dart';

class AuthService{
  static final url="https://cors-anywhere.herokuapp.com/https://packurbags.azurewebsites.net/api/";

  static Future<Response> register (String email,String username,String phone,String password,String firstname,) {
    final client = HttpClient();
    return post(url+'auth/register/',headers: <String,String>{
      'Content-Type': 'application/json',
      "Access-Control-Expose-Headers": "*",
    },
        body: jsonEncode(<String,String>{
          "email": email,
          "username": username,
          "password": password,
          "first_name": firstname,
          "last_name": "packurbags",
          "phone_number": phone,
        },));
  }

  static Future<Response> login (String email, String password) async{
    var abc =await get(url+'auth/login/');
    print(abc.headers);
    return post(url+'auth/login/',headers: <String,String>{
      'Content-Type': 'application/json',
      "Access-Control-Expose-Headers": "*",
    },
      body: jsonEncode(<String, String>{
        "email": email,
        "password": password,
      })
    );
  }
}




