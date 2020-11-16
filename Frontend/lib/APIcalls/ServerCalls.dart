import 'dart:io';

import 'package:http/http.dart';

class DataService{
  static final url="https://cors-anywhere.herokuapp.com/https://packurbags.azurewebsites.net/api/";

  static Future<Response> getCities(String token){
    print("In call"+ token);
    return get(
      url+"/city",
      headers: {
        "Authorization": 'Token $token',
      }
    );
  }

}