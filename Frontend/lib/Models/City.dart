import 'package:flutter/cupertino.dart';
import 'package:travel/Models/Guides.dart';

//change Notifier class
class City extends ChangeNotifier {
  String cityName;
  String state;
  String country;
  String pinCode;
  int cityID;
  String basicInfo;
  String imageURL;
  // list of id's of monuments
  List<int> monumentIDs;
  // list of id's of guides
  List<int> guideIDs;

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

  factory City.fromJSON(Map<String,dynamic> json){
    return City(
        cityName: json["city_name"],
        state: json["state"],
        country: json["country"],
        pinCode: json["pin_code"],
        cityID: json["city_id"],
        monumentIDs : json["monument_ids"],
        guideIDs: json["guide_ids"],
      basicInfo: json["city_info"],
      imageURL: json["imageURL"],
    );
  }

  populateFromJSON(Map<String, dynamic> json) {
      cityName= json["city_name"];
      state= json["state"];
      country= json["country"];
      pinCode= json["pin_code"];
      cityID= json["city_id"];
      monumentIDs = json["monument_ids"];
      guideIDs= json["guide_ids"];
  }
}

// 2 monument classes: 1 for displaying data on City's tab, 1 with ChangeNotifier for Monument's screen
class BasicMonument{
  int monumentID;
  String monumentName;
  String basicInfo;
  String imageURL;

  BasicMonument({
   this.monumentID,
   this.monumentName,
   this.basicInfo,this.imageURL,
});

  factory BasicMonument.fromJSON(Map<String,dynamic> json){
    return BasicMonument(
      monumentID: json["monument_id"],
      monumentName: json["monument_name"],
      basicInfo: json["basic_info"],
      imageURL: json["imageURL"],
    );
  }
}

