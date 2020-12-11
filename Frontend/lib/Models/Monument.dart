import 'package:flutter/cupertino.dart';

//ChangeNotifier class
class Monument extends ChangeNotifier {
  int monumentID;
  String monumentName;
  String city;
  String state;
  String country;
  String info;
  String cityID;
  String imageURL;
  List<int> guideIDs;

  Monument(
      {this.monumentID,
      this.monumentName,
      this.city,
      this.state,
      this.country,
      this.info,
      this.cityID,
      this.imageURL});

  factory Monument.fromJSON(Map<String, dynamic> json) {
    return Monument(
      monumentID: json["monument_id"],
      monumentName: json["monument_name"],
      city: json["city_name"],
      state: json["state"],
      country: json["country"],
      cityID: json["city_id"],
      info: json["basic_info"],
      imageURL: json["imageURL"],
    );
  }

  populatefromJSON(Map<String, dynamic> json) {
    monumentID = json["monument_id"];
    monumentName = json["monument_name"];
    city = json["city_name"];
    state = json["state"];
    country = json["country"];
    cityID = json["city_id"];
    info = json["basic_info"];
    imageURL = json["imageURL"];
  }
}
