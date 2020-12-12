import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

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

class Guide1{
  int guideID;
  String email;
  String name;
  String username;
  String phoneNum;
  String imageURL;
  List place;
  int cost;

  Guide1({this.guideID,this.email,this.name,this.phoneNum,this.username,this.place,this.imageURL,this.cost});

  factory Guide1.fromJSON(Map<String,dynamic> json){
    return Guide1(
      guideID: json["guide_id"],
      email: json["email"],
      name: json["first_name"]+ " "+json["last_name"],
      username: json["username"],
      phoneNum: json["phone_number"],
      place: json["place"],
      cost: 1300,
      imageURL: "https://image.shutterstock.com/image-vector/young-man-face-cartoon-260nw-1224888760.jpg",
    );
  }
}

class BookGuide extends ChangeNotifier {
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