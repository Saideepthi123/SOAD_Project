import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import 'package:travel/Models/Monument.dart';

class MonumentInfoTab extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final _screenSize=MediaQuery.of(context).size;
    final monument=Provider.of<Monument>(context);
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
                      // Flexible(child: Text("Highlights:	Indo-Saracenic style of architecture ",style: GoogleFonts.raleway(fontSize: 15),)),
                      // Flexible(child: Text("Nearby Tourist Attractions:	Elephanta Caves and Taj Mahal Palace Hotel ",style: GoogleFonts.raleway(fontSize: 15),)),
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
