class Hotels {
  int id;
  String name;
  String visitUrl;
  double ratings;
  Address address;
  String cost;

  Hotels(
      {this.id,
        this.name,
        this.visitUrl,
        this.ratings,
        this.address,
        this.cost});

  Hotels.fromJson(Map<String, dynamic> json) {
    id = json['id'];
    name = json['name'];
    visitUrl = json['visitUrl'];
    ratings = json['Ratings'];
    address =
    json['address'] != null ? new Address.fromJson(json['address']) : null;
    cost = json['cost'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['id'] = this.id;
    data['name'] = this.name;
    data['visitUrl'] = this.visitUrl;
    data['Ratings'] = this.ratings;
    if (this.address != null) {
      data['address'] = this.address.toJson();
    }
    data['cost'] = this.cost;
    return data;
  }
}

class Address {
  String address;
  String locality;
  String countryName;

  Address({this.address, this.locality, this.countryName});

  Address.fromJson(Map<String, dynamic> json) {
    address = json['address'];
    locality = json['locality'];
    countryName = json['countryName'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['address'] = this.address;
    data['locality'] = this.locality;
    data['countryName'] = this.countryName;
    return data;
  }
}
