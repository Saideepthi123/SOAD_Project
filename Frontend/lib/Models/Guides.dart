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