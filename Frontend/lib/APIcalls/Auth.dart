import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart';
import 'package:url_launcher/url_launcher.dart';

class AuthService {
  static final url =
      "https://cors-anywhere.herokuapp.com/https://packurbags.azurewebsites.net/api/";

  static Future<Response> register(
    String email,
    String username,
    String phone,
    String password,
    String firstname,
  ) {
    return post(url + 'auth/register/',
        headers: <String, String>{
          'Content-Type': 'application/json',
        },
        body: jsonEncode(
          <String, String>{
            "email": email,
            "username": username,
            "password": password,
            "first_name": firstname,
            "last_name": "packurbags",
            "phone_number": phone,
          },
        ));
  }

  static Future<Response> login(String email, String password) async {
    return post(url + 'auth/login/',
        headers: <String, String>{
          'Content-Type': 'application/json',
        },
        body: jsonEncode(<String, String>{
          "email": email,
          "password": password,
        }));
  }

  static Future<Response> logout(String token,String refreshToken) {
    return post(url + 'auth/logout/',
        headers: <String, String> {
          'Content-Type': 'application/json',
          "Authorization": 'Bearer $token',
        },
        body: jsonEncode(<String, String>{
          "refresh": refreshToken,
        })
    );
  }


  static launchGoogleAuth() async {
    // cors anywhere is blocked by google
    String gurl = url + 'auth/google-auth';
    print(gurl);
    if (await canLaunch(gurl)) {
      await launch(gurl,
        forceSafariVC: false,
        forceWebView: false,
        // headers: <String, String>{'my_header_key': 'my_header_value'},
      );

    } else {
      throw 'Could not launch $gurl';
    }
  }
}
