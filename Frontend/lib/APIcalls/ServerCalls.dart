import 'dart:convert';
import 'dart:io';

import 'package:http/http.dart';
import 'package:intl/intl.dart';

class DataService {
  static final url =
      "https://cors-anywhere.herokuapp.com/https://packurbags.azurewebsites.net/api";

  static Future<Response> getCities(String token) {
    // print("In call "+ token);
    print("$url/city");
    return get("$url/city", headers: {
      "Authorization": 'Bearer $token',
    });
  }

  static Future<Response> getMonumentFromCity(String token, int cityID) {
    return get("$url/city/$cityID/monuments", headers: {
      "Authorization": 'Bearer $token',
    });
  }

  static Future<Response> getMonuments(String token) {
    // print("In call "+ token);
    // print("$url/monument");
    return get("$url/monument", headers: {
      "Authorization": 'Bearer $token',
    });
  }

  static Future<Response> getCity(String token, int idx) {
    // print("In call "+ token);
    print("$url/city/$idx");
    return get(
      "$url/city/$idx",
      headers: {
        "Authorization": 'Bearer $token',
      },
    );
  }

  static Future<Response> getMonument(String token, int idx) {
    // print("In call "+ token);
    print("$url/monument/$idx");
    return get("$url/monument/$idx", headers: {
      "Authorization": 'Bearer $token',
    });
  }

  static Future<Response> searchFlights(
      String token, String origin, String dest, DateTime depDate) {
    var dateFormat = DateFormat('yyyy-MM-dd');
    // print("In call "+ token);
    print("$url/skyscanner/search-flights");
    return post("$url/skyscanner/search-flights",
        headers: <String, String>{
          'Content-Type': 'application/json',
          "Authorization": 'Bearer $token',
        },
        body: jsonEncode(
          <String, String>{
            "country": "IN",
            "currency": "INR",
            "locale": "en-IN",
            "originplace": origin,
            "destinationplace": dest,
            "outboundpartialdate": dateFormat.format(depDate),
          },
        ));
  }

  static Future<Response> getFood(String token, String city) {
    return get(
      "$url/zomato/search-city?city=$city",
      headers: {
        "Authorization": 'Bearer $token',
      },
    );
  }

  static Future<Response> getFoodLocality(String token, String locality) {
    return get(
      "$url/zomato/search-locality?q=$locality",
      headers: {
        "Authorization": 'Bearer $token',
      },
    );
  }

  static Future<Response> getHotels(String token, String City) {
    return post("$url/hotels/search-hotels",
        headers: {
          "Authorization": 'Bearer $token',
        },
        body: {
          "place": "$City",
          "locale": "en_IN",
          "pageNumber": "1",
          "checkIn": "2020-01-08",
          "checkOut": "2020-01-15",
          "pageSize": "25",
          "adults1": "1",
          "currency": "INR"
        });
  }

  static Future<Response> getGuides(String token) {
    // print("In call "+ token);
    print("$url/guide");
    return get("$url/guide", headers: {
      "Authorization": 'Bearer $token',
    });
  }

  static Future<Response> searchGuides(String token, String city,DateTime startDate,DateTime endDate) {
    var dateFormat = DateFormat('yyyy-MM-dd');
    return post("$url/guide/search/available-guides",
        headers: {
          "Authorization": 'Bearer $token',
        },
        body: {
          "start_date": dateFormat.format(startDate),
          "end_date": dateFormat.format(endDate),
          "city": city
        });
  }

  static Future<Response> launchPayment(int gid,int uid, int numDays){
    final payUrl= '$url/book-guides/$gid/$uid/$numDays';
    print(payUrl);
  }
}
