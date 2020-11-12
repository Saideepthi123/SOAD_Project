import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:travel/Models/City.dart';
import 'package:travel/Screens/Monument.dart';
import 'package:travel/Tools/Global%20tools.dart';

class MonumentInfoTab extends StatelessWidget {
  Monument monument = Monument.fromJSON({
    "monument_name": "Gateway Of India",
    "state": "Maharashtra",
    "city_name": "Mumbai",
    "country": "India",
    "city_id": "3",
    "basic_info": "The Gateway of India is an arch-monument built in the early twentieth century in the city of Mumbai, in the Indian state of Maharashtra. It was erected to commemorate the landing in December 1911 at Apollo Bunder, Mumbai of King-Emperor George V and Queen-Empress Mary, the first British monarch to visit India.",
    "imageURL": "https://www.travelogyindia.com/images/mumbai/gateway-of-india-tipl-1.jpg"
  });
  @override
  Widget build(BuildContext context) {
    final _screenSize=MediaQuery.of(context).size;
    return Container(
      padding: EdgeInsets.all(20),
      child: Card(
        elevation: 10,
        child: Container(
          height: _screenSize.height*0.3,
          padding: EdgeInsets.all(10),
          child: Column(
            children: [
              Flexible(
                child: Container(
                  padding: EdgeInsets.all(8),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      Flexible(child: Text(monument.monumentName, overflow: TextOverflow.ellipsis,style: GoogleFonts.raleway(
                    fontSize: 30
                  )
                      )),
                      Text(monument.city+ ", "+monument.state,overflow: TextOverflow.ellipsis,style: GoogleFonts.raleway(
                          fontSize: 20
                      )),
                      Flexible(child: Text(monument.info,style: GoogleFonts.raleway(fontSize: 15),)),
                      Flexible(child: Text("Highlights:	Indo-Saracenic style of architecture ",style: GoogleFonts.raleway(fontSize: 15),)),
                      Flexible(child: Text("Nearby Tourist Attractions:	Elephanta Caves and Taj Mahal Palace Hotel ",style: GoogleFonts.raleway(fontSize: 15),)),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
