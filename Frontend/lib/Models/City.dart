class City{
  String cityName;
  String state;
  String country;
  String pinCode;
  String cityID;
  String basicInfo;
  String imageURL;

  City({this.cityName,this.state,this.country,this.pinCode,this.cityID,this.imageURL});

  factory City.fromJSON(Map<String,dynamic> json){
    return City(
      cityName: json["city_name"],
      state: json["state"],
      country: json["country"],
      pinCode: json["pin_code"],
      cityID: json["city_id"],
    );
  }
}

class Monument{
  String monumentID;
  String monumentName;
  String city;
  String state;
  String country;
  String info;
  String cityID;
  String imageURL;

  Monument({this.monumentID,this.monumentName,
  this.city,this.state,this.country,this.info,this.cityID,this.imageURL});

  factory Monument.fromJSON(Map<String,dynamic> json){
    return Monument(
      monumentName: json["monument_name"],
      state: json["state"],
      country: json["country"],
      cityID: json["city_id"],
      info: json["basic_info"],
      imageURL: json["imageURL"],
    );
  }
}