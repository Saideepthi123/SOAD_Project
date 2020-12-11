import 'package:flutter/material.dart';

class Restaurant{
  String id;
  String name;
  String visitUrl;
  String cuisines;
  String timings;
  int cost2;
  String thumbImg;
  Map location;
  double rating;

  Restaurant({
   this.id,
   this.name,
   this.visitUrl,
   this.cuisines,
   this.timings,
   this.cost2,
   this.thumbImg,
   this.rating,
    this.location,
});

  factory Restaurant.fromJSON(Map<String,dynamic> json){
    return Restaurant(
      id: json["id"],
      name: json["name"],
      visitUrl: json["visitUrl"],
      location: json["location"],
      cuisines: json["cuisines"],
      timings: json["timings"],
      cost2: json["cost_for_2"],
      thumbImg: json["thumb"],
      rating: double.parse(json["rating"]),
    );
  }

}