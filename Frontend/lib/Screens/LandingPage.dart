import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:travel/Models/Image.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:travel/Screens/onboarding/loginSign.dart';

class HomeShelf extends StatefulWidget {
  @override
  _HomeShelfState createState() => _HomeShelfState();
}

class _HomeShelfState extends State<HomeShelf> {
  final _key = GlobalKey<AnimatedListState>();
  final myTween = Tween<Offset>(
    begin: const Offset(0.0, -1.0),
    end: Offset.zero,
  );

  @override
  Widget build(BuildContext context) {
    final screenSize= MediaQuery.of(context).size;
    var change = Provider.of<BackImage>(context);
    return Container(
      margin: EdgeInsets.symmetric(horizontal: 40, vertical: 20),
      child: Column(
        mainAxisSize: MainAxisSize.max,
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                "Travel",
                style: GoogleFonts.lato(
                    color: Colors.white,
                    fontSize: 40,
                    fontWeight: FontWeight.w900),
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  RaisedButton(
                    onPressed: (){
                      Navigator.push(context, MaterialPageRoute(builder: (context)=>LogIn()));
                    },
                    color: Colors.grey,
                    child: Text(
                      "Log In or Sign Up",
                      style: GoogleFonts.lato(
                          color: Colors.white,
                          fontSize: 18,
                          fontWeight: FontWeight.w300),
                    ),
                  ),
                  // SizedBox(
                  //   width: 10,
                  // ),
                  // Text(
                  //   "Option 2",
                  //   style: GoogleFonts.lato(
                  //       color: Colors.white,
                  //       fontSize: 18,
                  //       fontWeight: FontWeight.w300),
                  // ),
                  // SizedBox(
                  //   width: 10,
                  // ),
                  // Text(
                  //   "Option 3",
                  //   style: GoogleFonts.lato(
                  //       color: Colors.white,
                  //       fontSize: 18,
                  //       fontWeight: FontWeight.w300),
                  // ),
                ],
              ),
              IconButton(
                  icon: Icon(
                    Icons.search,
                    color: Colors.white,
                  ),
                  onPressed: null)
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Container(
                margin: EdgeInsets.only(left: 50),
                child: AnimatedSwitcher(
                  duration: Duration(milliseconds: 700),
                  transitionBuilder:
                      (Widget child, Animation<double> animation) {
                    return SlideTransition(
                      child: child,
                      position: Tween<Offset>(
                              begin: Offset(0.0, -1.0),
                              end: Offset(0.0, 0.0))
                          .animate(animation),
                    );
                  },
                  child: Container(
                    key: Key(change.cityname),
                    child: Column(
                      children: [
                        Text(
                          change.cityname,
                          style: GoogleFonts.lato(
                              color: Colors.white,
                              fontSize: 52,
                              fontWeight: FontWeight.w900),
                        ),
                        Text(change.metadata,
                          style: GoogleFonts.lato(
                              color: Colors.white,
                              fontSize: 18,
                              fontWeight: FontWeight.w500),

                        overflow: TextOverflow.ellipsis,)
                      ],
                    ),
                  ),
                ),
              ),
              Container(
                width: screenSize.width*0.5,
                height: screenSize.height*0.45,
                child: AnimatedList(
                    key: _key,
                    scrollDirection: Axis.horizontal,
                    initialItemCount: change.cities.length,
                    itemBuilder: (context, index, animation) {
                      return SlideTransition(
                        position: animation.drive(myTween),
                        child: InkWell(
                          onTap: () {
                            change.currimage(change.cities[index]);
                            change.cityname = change.cities[index];
                            print(change.cities);
                          },
                          child: Card(
                            shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(20)),
                            elevation: 30,
                            color: Colors.white,
                            margin: EdgeInsets.symmetric(horizontal: 20),
                            child: Container(
                              decoration: BoxDecoration(
                                  borderRadius: BorderRadius.circular(20),
                                  image: DecorationImage(
                                      image: AssetImage('./img/CardImage' +
                                          change.cities[index] +
                                          '.jpg'),
                                      fit: BoxFit.cover)),
                              height: screenSize.height*0.45,
                              width: screenSize.width*0.15,
                              child: Column(
                                mainAxisAlignment: MainAxisAlignment.end,
                                children: [
                                  Text(
                                    change.cities[index],
                                    style: GoogleFonts.lato(
                                        color: Colors.white,
                                        fontSize: 32,
                                        fontWeight: FontWeight.w900),
                                  ),
                                  SizedBox(
                                    height: 10,
                                  )
                                ],
                              ),
                            ),
                          ),
                        ),
                      );
                    }),
              ),
            ],
          ),
          Container(),
        ],
      ),
    );
  }
}
