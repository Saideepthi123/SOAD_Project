import 'package:flutter/cupertino.dart';
import 'package:travel/Models/Guides.dart';

//change Notifier class
class City {
  String cityName;
  String state;
  String country;
  String pinCode;
  String cityID;
  String basicInfo;
  String imageURL;
  // list of id's of monuments
  List<int> monumentIDs;
  // either retrieve and save once, or retrieve with ID's every time
  // List<BasicMonument> monuments

  // list of id's of guides
  List<int> guideIDs;
  // either retrieve and save once, or retrieve with ID's every time
  // List<Guide> guides;

  City({
    this.cityName,
    this.state,
    this.country,
    this.pinCode,
    this.cityID,
    this.basicInfo,
    this.imageURL,
    this.monumentIDs,
    this.guideIDs,
  });

  factory City.fromJSON(Map<String, dynamic> json) {
    return City(
      cityName: json["city_name"],
      state: json["state"],
      country: json["country"],
      pinCode: json["pin_code"],
      cityID: json["city_id"],
      //if ID's, retrieve them with future builder/stream builder
      monumentIDs: json["monument_ids"],
      guideIDs: json["guide_ids"],

    //  if not
    //   monuments: populate from ids
    //  cities: populate from ids
    );
  }
}

// 2 monument classes: 1 for displaying data on City's tab, 1 with ChangeNotifier for Monument's screen
class BasicMonument{
  int monumentID;
  String monumentName;
  String basicInfo;

  BasicMonument({
   this.monumentID,
   this.monumentName,
   this.basicInfo,
});
}

//ChangeNotifier class
class Monument{
  String monumentID;
  String monumentName;
  String city;
  String state;
  String country;
  String info;
  String cityID;
  String imageURL;
  List<int> guideIDs;
  // List<Guide> guides;
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
      monumentName: json["monument_name"],
      city: json["city_name"],
      state: json["state"],
      country: json["country"],
      cityID: json["city_id"],
      info: json["basic_info"],
      imageURL: json["imageURL"],
    );
  }
}
