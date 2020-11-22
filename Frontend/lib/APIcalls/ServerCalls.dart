import 'dart:io';

import 'package:http/http.dart';

class DataService{
  static final url="https://cors-anywhere.herokuapp.com/https://packurbags.azurewebsites.net/api";

  static Future<Response> getCities(String token){
    print("In call "+ token);
    print("$url city");
    return get(
      "$url/city",
      headers: {
        "Authorization": 'Bearer $token',
      }
    );
  }

  static Future<Response> getMonuments(String token){
    print("In call "+ token);
    print("$url/monument");
    return get(
        "$url/monument",
        headers: {
          "Authorization": 'Bearer $token',
        }
    );
  }

  static Future<Response> getCity(String token,String city){
    print("In call "+ token);
    print("$url/city?q={\"name\":$city}");
    return get(
        "$url/city?q={\"name\":$city}",
        headers: {
          "Authorization": 'Bearer $token',
        }
    );
  }

  static Future<Response> getMonument(String token, String monument){
    print("In call "+ token);
    print("$url/monument?q={\"name\":$monument}");
    return get(
        "$url/monument?q={\"name\":$monument}",
        headers: {
          "Authorization": 'Bearer $token',
        }
    );
  }

}