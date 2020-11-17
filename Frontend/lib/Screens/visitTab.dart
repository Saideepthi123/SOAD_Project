import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart';
import 'package:provider/provider.dart';
import 'package:travel/APIcalls/ServerCalls.dart';
import 'package:travel/Models/City.dart';
import 'package:travel/Models/Monument.dart';
import 'package:travel/Models/User.dart';
import 'package:travel/Screens/Monument.dart';
import 'package:travel/Tools/Global%20tools.dart';

class VisitTab extends StatelessWidget {
  BasicMonument basicMonument = BasicMonument.fromJSON({
    "monument_id": 1,
    "monument_name": "Gateway Of India",
    "basic_info":
        "The Gateway of India is an arch-monument built in the early twentieth century in the city of Mumbai, in the Indian state of Maharashtra.",
    "imageURL":
        "https://www.travelogyindia.com/images/mumbai/gateway-of-india-tipl-1.jpg"
  });

  Map<String,dynamic> json = {
    "monument_id": 1,
    "monument_name": "Gateway Of India",
    "state": "Maharashtra",
    "city_name": "Mumbai",
    "country": "India",
    "city_id": "3",
    "basic_info":
        "The Gateway of India is an arch-monument built in the early twentieth century in the city of Mumbai, in the Indian state of Maharashtra. It was erected to commemorate the landing in December 1911 at Apollo Bunder, Mumbai of King-Emperor George V and Queen-Empress Mary, the first British monarch to visit India.",
    "imageURL":
        "https://www.travelogyindia.com/images/mumbai/gateway-of-india-tipl-1.jpg"
  };
  @override
  Widget build(BuildContext context) {
    final _screenSize = MediaQuery.of(context).size;
    final userModel=Provider.of<User>(context);
    return Container(
      padding: EdgeInsets.all(20),
      child: Column(
        children: [
          //  search bar
          SearchBar(
            width: _screenSize.width * 0.4,
            onChange: (val) {
              print(val);
            },
          ),
          Padding(
            padding: EdgeInsets.all(_screenSize.height * 0.01),
          ),
          //  cards
          Container(
            height: _screenSize.height * 0.6,
            child: ListView.separated(
              shrinkWrap: true,
              itemCount: 8,
              separatorBuilder: (context, idx) {
                return Padding(
                  padding: EdgeInsets.all(10),
                );
              },
              itemBuilder: (context, idx) {
                return InkWell(
                      onTap: () {
                        // monument.populatefromJSON(json);
                        Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) => FutureBuilder<Object>(
                                  future: DataService.getMonuments(userModel.token),
                                  builder: (context, snapshot) {
                                    if(snapshot.connectionState==ConnectionState.done){
                                      if(snapshot.hasData){
                                        Response response=snapshot.data;
                                        print(response.body);
                                        return ChangeNotifierProvider<Monument>(
                                            create: (_) => Monument.fromJSON(json),
                                            child: MonumentPage());
                                      }
                                      if(snapshot.hasError){
                                        return Container(
                                          child: Text("404 Page Not Found"),
                                        );
                                      }
                                    }
                                    return Center(
                                        child: Image.asset(
                                          "pageLoading.gif",
                                          height: _screenSize.height*0.9,
                                          width: _screenSize.height*0.9,
                                        )
                                    );
                                  }
                                )
                            )
                        );
                      },
                      child: Card(
                        elevation: 10,
                        child: Container(
                          height: _screenSize.height * 0.3,
                          padding: EdgeInsets.all(10),
                          child: Row(
                            children: [
                              Image.network(
                                basicMonument.imageURL,
                                fit: BoxFit.fill,
                                loadingBuilder: (BuildContext context,
                                    Widget child,
                                    ImageChunkEvent loadingProgress) {
                                  if (loadingProgress == null) return child;
                                  return Center(
                                    child: CircularProgressIndicator(
                                      value: loadingProgress
                                                  .expectedTotalBytes !=
                                              null
                                          ? loadingProgress
                                                  .cumulativeBytesLoaded /
                                              loadingProgress.expectedTotalBytes
                                          : null,
                                    ),
                                  );
                                },
                              ),
                              Flexible(
                                child: Container(
                                  padding: EdgeInsets.all(8),
                                  child: Column(
                                    crossAxisAlignment:
                                        CrossAxisAlignment.start,
                                    mainAxisAlignment:
                                        MainAxisAlignment.spaceEvenly,
                                    children: [
                                      Flexible(
                                          child: Text(
                                        basicMonument.monumentName,
                                        overflow: TextOverflow.ellipsis,
                                        style: TextStyle(fontSize: 30),
                                      )),
                                      Flexible(
                                          child: Text(
                                              basicMonument.basicInfo,
                                        style: TextStyle(fontSize: 15),
                                      )),
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
