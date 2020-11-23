
import 'package:intl/intl.dart';

class Flight{
  String carrierName;
  int minPrice;
  bool direct;
  DateTime departureDate;

  Flight({
   this.carrierName,
   this.minPrice,
    this.departureDate,
    this.direct,
});

  factory Flight.fromJSON(Map<String,dynamic> json){
    return Flight(
      carrierName: json["CarrierName"],
      minPrice: json["MinPrice"],
      direct: json["Direct"],
      departureDate: DateTime.parse(json["DepartureDate"]),
    );
  }
}