import 'package:flutter/cupertino.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

class Guide{
  int guideID;
  String guideName;
  int rating;
  String city;
  List<String> monumentNames;
  String imageURL;
  String price;

  Guide({this.guideID,this.guideName,this.rating,this.city,this.monumentNames,this.price,this.imageURL});

  factory Guide.fromJSON(Map<String,dynamic> json){
    return Guide(
      guideName: json["guide_name"],
      guideID: json["guide_id"],
      rating: json["rating"],
      city: json["place"],
      monumentNames: json["monumentNames"],
      imageURL: json["imageURL"],
    );
  }
}

class BookGuide extends ChangeNotifier{
  DateTime startDate=DateTime.now();
  DateTime endDate=DateTime.now();
  String type="Pay by hour";
  int guideID;


  updateGuide(int id){
    guideID=id;
  }

  updateStartDate(DateTime sD){
    startDate=sD;
    notifyListeners();
  }

  updateEndDate(DateTime eD){
    endDate=eD;
    notifyListeners();
  }

  updateType(String type0){
    type=type0;
    notifyListeners();
  }
}