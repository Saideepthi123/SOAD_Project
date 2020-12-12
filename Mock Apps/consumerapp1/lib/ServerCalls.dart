import 'dart:convert';
import 'dart:io';

import 'package:http/http.dart';
import 'package:intl/intl.dart';

class DataService {
  static final url =
      "https://cors-anywhere.herokuapp.com/https://packurbags.azurewebsites.net/api";


  static Future<Response> getToken(){
    print("get token");
    return get("$url/get-api-key?pk=1",headers: {
      "X-Requested-With": "XMLHttpRequest"
    },);
  }

  static Future<Response> getGuides(String token) {
    // print("In call "+ token);
    print("$url/guide/expose/$token");
    return get("$url/guide/expose/$token",headers: {
      "X-Requested-With": "XMLHttpRequest"
    },);
  }
}
