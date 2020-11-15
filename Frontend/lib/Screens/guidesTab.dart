import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:travel/Models/Guides.dart';
import 'package:travel/Tools/GuideFilter.dart';

class GuidesTab extends StatefulWidget {
  @override
  _GuidesTabState createState() => _GuidesTabState();
}

class _GuidesTabState extends State<GuidesTab> {
  DateTime _startDate;
  DateTime _endDate;

  Guide guide = Guide.fromJSON({
    "guide_name": "Chandler Bing",
    "guide_id": 2,
    "rating": 3.0,
    "monument_names": ["Monument A","Monument B"],
    "imageURL": "https://image.shutterstock.com/image-vector/young-man-face-cartoon-260nw-1224888760.jpg"
  });

  @override
  Widget build(BuildContext context) {
    final _screenSize = MediaQuery.of(context).size;
    return ChangeNotifierProvider(
      create: (_) => BookGuide(),
      child: Container(
        padding: EdgeInsets.all(20),
        child: Column(
          children: [
            //  guide filter
            GuideFilter(
              width: _screenSize.width*0.6,
            ),
            Padding(
              padding: EdgeInsets.all(_screenSize.height * 0.01),
            ),
            //  cards
            Container(
              height: _screenSize.height * 0.55,
              child: ListView.separated(
                shrinkWrap: true,
                itemCount: 8,
                separatorBuilder: (context, idx) {
                  return Padding(
                    padding: EdgeInsets.all(8),
                  );
                },
                itemBuilder: (context, idx) {
                  return Card(
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
                                    guide.guideName,
                                    overflow: TextOverflow.ellipsis,
                                    style: TextStyle(fontSize: 30),
                                  )),
                                  Row(
                                    children: [
                                  Text(
                                  "Rating: " + guide.rating.toString(),
                            overflow: TextOverflow.ellipsis,
                            style: TextStyle(fontSize: 20),
                          ),

                                      Icon(
                                          Icons.star
                                      ),
                                    ],
                                  )

                                ],
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  );
                },
              ),
            )
          ],
        ),
      ),
    );
  }
}
