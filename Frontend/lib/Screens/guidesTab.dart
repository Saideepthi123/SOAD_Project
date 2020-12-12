import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:http/http.dart';
import 'package:provider/provider.dart';
import 'package:stripe_payment/stripe_payment.dart';
import 'package:travel/APIcalls/ServerCalls.dart';
import 'package:travel/Models/City.dart';
import 'package:travel/Models/Guides.dart';
import 'package:travel/Models/User.dart';
import 'package:travel/Tools/GuideFilter.dart';

class GuidesTab extends StatefulWidget {
  @override
  _GuidesTabState createState() => _GuidesTabState();
}

class _GuidesTabState extends State<GuidesTab> {
  DateTime _startDate;
  DateTime _endDate;
  bool isSet = false;
  Source _source;
  PaymentMethod _paymentMethod;
  String _error;
  final String _currentSecret = null;

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
  }

  var guide = Guide.fromJSON({
    "guide_name": "Chandler Bing",
    "guide_id": 2,
    "rating": 3.0,
    "monument_names": ["Monument A","Monument B"],
    "imageURL": "https://image.shutterstock.com/image-vector/young-man-face-cartoon-260nw-1224888760.jpg"
  });

  _setSet(){
    print("hit");
    setState(() {
      isSet=true;
    });
  }

  void setError(dynamic error) {
    // _scaffoldKey.currentState.showSnackBar(SnackBar(content: Text(error.toString())));
    setState(() {
      _error = error.toString();
    });
    print(_error);
  }

  final CreditCard testCard = CreditCard(
    number: '4000002760003184',
    expMonth: 12,
    expYear: 21,
  );

  _showPaymentDialog(Guide1 guide1,int uid,int numDays){
    return showDialog<void>(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Book Guide : '+ guide1.name),
          content: Text('Pay in INR: '+ guide1.cost.toString()),
          actions: <Widget>[
            FlatButton(
              child: Text('Continue Payment'),
              onPressed: () {
                DataService.launchPayment(guide1.guideID,uid,numDays);
        },
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final _screenSize = MediaQuery.of(context).size;
    final userModel=Provider.of<User>(context);
    final cityModel=Provider.of<City>(context);
    return ChangeNotifierProvider(
      create: (_) => BookGuide(),
      child: Container(
        padding: EdgeInsets.all(20),
        child: Column(
          children: [
            //  guide filter
            GuideFilter(
              width: _screenSize.width*0.6,
              onDone: _setSet(),
            ),
            Padding(
              padding: EdgeInsets.all(_screenSize.height * 0.01),
            ),
            //  cards
            Consumer<BookGuide>(
              builder: (context, bookGuide, child){
                return Container(
                  width: _screenSize.width*0.6,
                  height: _screenSize.height * 0.55,
                  child: FutureBuilder(
                      future: isSet ? DataService.searchGuides(userModel.token,cityModel.cityName , bookGuide.startDate,bookGuide.endDate) :
                      DataService.getGuides(userModel.token),
                      builder: (context, snapshot) {
                        if(snapshot.connectionState==ConnectionState.done){
                          if(snapshot.hasData){
                            Response response=snapshot.data;
                            if(response.statusCode==200){
                              List json = jsonDecode(response.body);
                              return ListView.separated(
                                shrinkWrap: true,
                                itemCount: json.length,
                                separatorBuilder: (context, idx) {
                                  return Padding(
                                    padding: EdgeInsets.all(8),
                                  );
                                },
                                itemBuilder: (context, idx) {
                                  Guide1 guide=Guide1.fromJSON(json[idx]);
                                  return InkWell(
                                    onTap: (){
                                      print(userModel.uid);
                                      int numDays=bookGuide.startDate.difference(bookGuide.endDate).inDays;
                                      _showPaymentDialog(guide,1,-numDays);
                                    },
                                    child: Card(
                                      elevation: 10,
                                      child: Container(
                                        height: _screenSize.height * 0.3,
                                        padding: EdgeInsets.all(10),
                                        child: Row(
                                          children: [
                                            Image.network(
                                              guide.imageURL,
                                              fit: BoxFit.fill,
                                              loadingBuilder: (BuildContext context, Widget child,
                                                  ImageChunkEvent loadingProgress) {
                                                if (loadingProgress == null) return child;
                                                return Center(
                                                  child: CircularProgressIndicator(
                                                    value: loadingProgress.expectedTotalBytes !=
                                                        null
                                                        ? loadingProgress.cumulativeBytesLoaded /
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
                                                  crossAxisAlignment: CrossAxisAlignment.start,
                                                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                                                  children: [
                                                    Flexible(
                                                        child: Text(
                                                          guide.name,
                                                          overflow: TextOverflow.ellipsis,
                                                          style: GoogleFonts.raleway(
                                                              fontSize: 30,
                                                          ),
                                                        )),
                                                    Flexible(
                                                        child: Text(
                                                          guide.username,
                                                          overflow: TextOverflow.ellipsis,
                                                          style: GoogleFonts.raleway(
                                                            fontSize: 20,
                                                        ),
                                                        )),
                                                    Flexible(
                                                        child: Text(
                                                          guide.email,
                                                          overflow: TextOverflow.ellipsis,
                                                          style: GoogleFonts.raleway(
                                                              fontSize: 20,
                                                          ),
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
                              );
                            }
                          }
                          if(snapshot.hasError){
                            return Container(
                              child: Text("Page Not Found"),
                            );
                          }
                        }
                        return Center(child: CircularProgressIndicator());
                      }
                  ),
                );
              },
            )
          ],
        ),
      ),
    );
  }
}
