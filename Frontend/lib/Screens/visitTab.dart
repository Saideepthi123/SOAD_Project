import 'package:flutter/material.dart';
import 'package:travel/Models/City.dart';
import 'package:travel/Screens/Monument.dart';
import 'package:travel/Tools/Global%20tools.dart';

class VisitTab extends StatelessWidget {
  Monument monument = Monument.fromJSON({
    "monument_name": "Gateway Of India",
    "state": "Maharashtra",
    "country": "India",
    "city_id": "3",
    "basic_info": "The Gateway of India is an arch-monument built in the early twentieth century in the city of Mumbai, in the Indian state of Maharashtra.",
    "imageURL": "https://www.travelogyindia.com/images/mumbai/gateway-of-india-tipl-1.jpg"
  });
  @override
  Widget build(BuildContext context) {
    final _screenSize=MediaQuery.of(context).size;
    return Container(
      padding: EdgeInsets.all(20),
      child: Column(
        children: [
        //  search bar
        SearchBar(
          width: _screenSize.width*0.4,
          onChange: (val){
            print(val);
          },
        ),
        Padding(
          padding: EdgeInsets.all(_screenSize.height*0.01),
        ),
        //  cards
          Container(
            height: _screenSize.height*0.6,
            child: ListView.separated(
              shrinkWrap: true,
              itemCount: 8,
              separatorBuilder: (context,idx){
                return Padding(
                  padding: EdgeInsets.all(10),
                );
              },
              itemBuilder: (context,idx){
                return InkWell(
                  onTap: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context) => MonumentPage()));
                  },
                  child: Card(
                    elevation: 10,
                      child: Container(
                        height: _screenSize.height*0.3,
                      padding: EdgeInsets.all(10),
                      child: Row(
                        children: [
                          Image.network(monument.imageURL,fit: BoxFit.fill,
                            loadingBuilder:(BuildContext context, Widget child,ImageChunkEvent loadingProgress) {
                              if (loadingProgress == null) return child;
                              return Center(
                                child: CircularProgressIndicator(
                                  value: loadingProgress.expectedTotalBytes != null ?
                                  loadingProgress.cumulativeBytesLoaded / loadingProgress.expectedTotalBytes
                                      : null,
                                ),
                              );
                            },
                          ),
                          Flexible(
                            child: Container(
                              padding: EdgeInsets.all(8),
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                                children: [
                                  Flexible(child: Text(monument.monumentName, overflow: TextOverflow.ellipsis,style: TextStyle(fontSize: 30),)),
                                  Text("State: "+monument.state,overflow: TextOverflow.ellipsis,style: TextStyle(fontSize: 20),),
                                  Flexible(child: Text(monument.info,style: TextStyle(fontSize: 15),)),
                                ],
                              ),
                            ),
                          ),
                        ],
                      ),
                      ),
                    ),
                );
              },
            ),
          )
        ],
      ),
    );
  }
}
