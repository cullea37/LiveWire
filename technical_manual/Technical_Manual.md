** LiveWire Technical Manual**

**CA326 **

**Andrew Cullen, Daniel Rowe, Eoin McKeever**

**6th March 2020 **


<table>
  <tr>
   <td>
<h2><strong>0. Table of contents</strong></h2>

<strong>1. Introduction</strong>
<p>
<strong>   1.1. Overview</strong>
<p>
<strong>   1.2. Glossary</strong>
<p>
<strong>   1.3 Starting design vs Finished design</strong>
<p>
<strong>2. System Architecture</strong>
<p>
<strong>2.1 System architecture diagram</strong>
<p>
<strong>3. High Level Design</strong>
<p>
<strong>3.1 Data Flow Diagrams</strong>
<p>
<strong>3.2 User flow diagram</strong>
<p>
<strong>3.3 Class Diagrams</strong>
<p>
<strong>3.4 State Diagram Sign in/Signup</strong>
<p>
<strong>3.5 State diagram Local page scroll </strong>
<p>
<strong>4. Problems and Resolutions</strong>
<p>
<strong>   4.1 Facebook Graph API</strong>
<p>
<strong>   4.2 Using Firebase cloud functions</strong>
<p>
<strong>   4.3 Crashes due to overload of data from database</strong>
<p>
<strong>   4.4  FireBase/Firestone beta features</strong>
<p>
<strong>5. Installation Guide</strong>
<p>
<strong>6. Testing</strong>
<p>
<strong>   6.1 User testing</strong>
<p>
<strong>   6.2 Use case testing</strong>
<h2><strong>1. Introduction</strong></h2>


<p>
<strong>1.1 Overview</strong>
<p>
The product is an Android app which notifies users of upcoming concert events and ticket releases in their local area. It’s aim is to act as a social platform for users to share their tastes and experiences by giving them the ability to rate events that have happened and let their followers know they are to be attending specific events.The project was designed so users could discover new music from their prior taste and from the people they choose to follow. Using the Spotify API we will pull a user's music preferences once they link their own Spotify account to their LiveWire account. Using this information taken from their Spotify account it helps our recommender make music and artist recommendations. Each profile will have a unique scrolling feed based on what recommendations the recommender provides. Each profile will also have their own customizable profile page where they can share their tastes and preferences. The concert recommender will use the ticketmaster API to find concerts and gigs in a user local area the listings are further filtered by their preferences. The app will have 4 main pages. They are the main scrolling page, the user profile page, the feed based on a user location and a settings page.The scrolling pages consists of listings of different artists. The profile page is the user's unique page that they customize themself. Finally the settings page will be where the user can change their preferences and share their location with the app. They can also link their social accounts to their LiveWire account here. The system stores users profile details and login credentials by using the service Firebase. Which safely stores user data once linked correctly. The project is made with Android Studio which makes linking these third party services quite convenient.
<p>
<strong>1.2 Glossary</strong>
<p>
<strong>API - </strong>Application Program Interface. A set of protocols to mandate how software components (usually in a client-server relationship) interact. In essence, a way to access some resource in a restricted/structured manner.
<p>
<strong>System - </strong>Defined very loosely as a set of functions, procedures, “things” and inputs interacting together towards some common goal. 
<p>
<strong>Cloud Functions- </strong> Google Cloud Functions is a serverless execution environment for building and connecting cloud services.
<p>
<strong>Location Based Services - </strong>Services that make use of a user’s location to provide some functionality. For example, using a phone’s GPS to set their standard language on startup.
<p>
<strong>Recommender system - </strong>A way to filter information to match with some criteria that fulfills a user’s expectations. In the context of LiveWire, this would be the filtering of concerts to find ones the user would enjoy going to. 
<p>
<strong>Recyclerview - </strong>Gives a fixed sized window to load a large dataset into.It recycles the views it created at the beginning when the views go out of scope.
<p>
<strong>Scope - </strong>the extent of the area or subject matter that something deals with or to which it is relevant.
<p>
<strong>1.3 Starting design vs Finished design</strong>
<p>
The project that we developed contains the core functionality that was specified in the functional spec. Users can make an account with us where their profile will be stored in our database. They can edit their page and scroll their feed and receive notifications and link their 3rd party accounts. Due to time constraints a follower system did not get implemented. We did not get to use the Facebook Graph API as we specified in our functional spec due to change in policy by Facebook we did not predict. We decided on the ticketmaster API but this cost us some development time. The time constraints on this project forced us to scrap a few features they include Facebook Profile Linker, Featured Song from a Concerts Artists,Follow User Feature, Concert Interactions ratings,Song and Playlist Sharing. We prioritised the implementation of the key features that are necessary to effectively demonstrate the app. Based on our work we have done throughout the year we believe if the given deadline was 1-2 weeks longer the app would have been finished in its totality.
<p>
Below is a list of system functions compared from start design to finished.

<table>
  <tr>
   <td>System Functions
   </td>
   <td>Degree of compliance
   </td>
  </tr>
  <tr>
   <td>Sign Up
   </td>
   <td>Done
   </td>
  </tr>
  <tr>
   <td>Sign in
   </td>
   <td>Done
   </td>
  </tr>
  <tr>
   <td>Concert Listings
   </td>
   <td>Done
   </td>
  </tr>
  <tr>
   <td>Link User Data API(s)
   </td>
   <td>Done with Partial Re-designed
   </td>
  </tr>
  <tr>
   <td>Profile Customization
   </td>
   <td>Done
   </td>
  </tr>
  <tr>
   <td>Posts
   </td>
   <td>Done
   </td>
  </tr>
  <tr>
   <td>Notifications
   </td>
   <td>Done
   </td>
  </tr>
  <tr>
   <td>User Feed
   </td>
   <td>Partially Done
   </td>
  </tr>
  <tr>
   <td>Filtering Concert Listings
   </td>
   <td>Partially done
   </td>
  </tr>
  <tr>
   <td>Rudimentary recommender system
   </td>
   <td>Partially done
   </td>
  </tr>
  <tr>
   <td>Facebook Profile Linker
   </td>
   <td>Scrapped
   </td>
  </tr>
  <tr>
   <td>Featured Song from a Concerts Artists
   </td>
   <td>Not done
   </td>
  </tr>
  <tr>
   <td>Concert Interactions ratings
   </td>
   <td>Not done
   </td>
  </tr>
  <tr>
   <td>Song and Playlist Sharing
   </td>
   <td>Scrapped
   </td>
  </tr>
  <tr>
   <td>Follow User Feature
   </td>
   <td>Not done
   </td>
  </tr>
</table>



## **2. System Architecture**

This section describes the high-level overview of the system architecture showing the distribution functions across system modules shown using the following diagram.It consists of a user interacting with the android app. The app communicates with three 3rd party services : Firebase Service,Spotify API and TicketMaster API. The app will query the API’s and pull account data. Also the app works with Firebase services to store data created from the running the app i.e user login details, user created content and user concert listings. Firebase services also include cloud based functions which updates user feed when new listings every night, when user signs up and links Spotify account finds recommended artists with help of cloud functions and spotify's API and links listings to user notifications and updates user listing feed as account develops.

**2.1 System architecture diagram**




![](https://gitlab.computing.dcu.ie/cullea37/2020-ca326-livewire/raw/master/technical_manual/System_Architecture2.1.png)


## **3. High-Level Design**

**3.1 Data Flow Diagrams**

This section consists of a data flow diagram that covers at a high level how the system interacts. The user interacts with D1 in three ways firstly a new user can register an account and store new login details in the database D1. Once stored the user can now enter these login details and the login details are compared to the database to see if they exist within the database. The user can also link their 3rd party accounts to the app and these can be saved to the database also. Once logged in a user gets filtered concert listings that comes from D2 the concert database which is filled by ticketmaster API these listings are filtered and sent back to the user. The user may with a created profile update their avatar and have it saved to D3 the user content Database. The user may also post to their page and have it stored in D3




![](https://gitlab.computing.dcu.ie/cullea37/2020-ca326-livewire/raw/master/technical_manual/Data_Flow_Diagram3.1.png)

**3.2 User flow diagram**

This diagram shows the user flow. When the application is installed the user can make a LW profile from here they have the option to link 3rd party music sources i.e Spotify if they choose to they can continue to find music events they can also choose to not link and attempt to find music events. They will not receive an event feed tailored to their preferences this way. Users can then scroll through their feed of music events and will receive continuous notifications based off their sources and interactions.




![](https://gitlab.computing.dcu.ie/cullea37/2020-ca326-livewire/raw/master/technical_manual/User_Flow_Diagram3.2.png)

**3.3 Class Diagrams**

The following diagram shows classes and their relationships.




![](https://gitlab.computing.dcu.ie/cullea37/2020-ca326-livewire/raw/master/technical_manual/Class_Diagram_3.3.png)

**3.4 State Diagram Sign in/Signup**




![](https://gitlab.computing.dcu.ie/cullea37/2020-ca326-livewire/raw/master/technical_manual/State_Diagram_Signin_Up3.4.png)

**3.5 State diagram Local page scroll **




![](https://gitlab.computing.dcu.ie/cullea37/2020-ca326-livewire/raw/master/technical_manual/State_Diagram_Local3.5.png)

## **4. Problems and Resolution**

Throughout the design of this project we encountered problems like any project does.I will go into 4 of the major ones. Firstly our attempted use of the Facebook API,using FIrebase cloud functions, bugs due to overload of data and using certain features in firebase and firestore which have certain features still in beta.

**4.1. Facebook Graph API**

One problem was the use of the Facebook graph API. We found later in the project that the use of the Facebook API came with certain conditions that Facebook specified but we were not aware of. This meant we were forced to find another way to suggest listings in a users local area and to find new friend listings.

In future projects we will use a mix of different API’s to achieve a similar effect to what Facebook API supplies. But due to time constraints we chose to use the Ticketmaster API.

**4.2 Using Firebase’s cloud functions**

Another issue we ran into was using the Firebase in-built cloud functions. We found that on the the level of Firebase plan we had available to us we could not use these in-built cloud functions in association with our API calls because we did not own the required version of firebase.

In future projects we will be able to bite the bullet and pay to upgrade our FIrebase account to a premium plan.

**4.3 Crashes due to overload of data from database**

When we introduced data into our scrolling feed we were met with a crash due to the app trying to load all the data we had into the feed.

In future projects we will make sure to firstly implement a recyclerview that acts as a block to stop the app continually loading data and only loads data when requested. Which is what we ended up doing.

**4.4 FireBase/Firestone beta features**

We chose to use FireBase and FireStone along with their included features when dealing with data in our application. SO because of this we made the decision to work with some of their included features some of which are still in Beta version.

In future projects we will search for an alternative solution to avoid using these features by researching other services that supply these tools.

As expected from a large group project we ran into some issues. But as a whole we felt the issues were dealt with as effectively as possible within the timeframe given.


## **5. Installation Guide**

**Step 1:**

To install this app a user must have access to an android device with a version of Android 9.0 or higher. 

**Step 2:**

The app will be available to download from the google play store which is available on all devices with android OS. But until it is released the app will be available in a APK file which can be received by email by getting in contact with any of the developers.

**Step 3:**

A user will simply search our apps name into the google play store and click on the install button next to our apps link. Or they will click on the executable APK file they have received by email

**Step 4:**

The app will then be available to open on your device from the unique icon on the menu.

**6 Testing**

**6.1 User Testing**




![](https://gitlab.computing.dcu.ie/cullea37/2020-ca326-livewire/raw/master/technical_manual/User_Testing1.PNG)


![](https://gitlab.computing.dcu.ie/cullea37/2020-ca326-livewire/raw/master/technical_manual/User_Testing2.PNG)


![](https://gitlab.computing.dcu.ie/cullea37/2020-ca326-livewire/raw/master/technical_manual/User_Testing3.PNG)


![](https://gitlab.computing.dcu.ie/cullea37/2020-ca326-livewire/raw/master/technical_manual/User_Testing4.PNG)


![](https://gitlab.computing.dcu.ie/cullea37/2020-ca326-livewire/raw/master/technical_manual/User_Testing5.PNG)



**6.2 Use Case Testing**


<table>
  <tr>
   <td><strong>No.</strong>
   </td>
   <td><strong>Job</strong>
   </td>
   <td><strong>Steps</strong>
   </td>
   <td><strong>Status</strong>
   </td>
  </tr>
  <tr>
   <td><strong>1</strong>
   </td>
   <td><strong>Sign up</strong>
   </td>
   <td>
<ol>

<li><strong>Press “SignUp” button</strong>

<li><strong>Enter email</strong>

<li><strong>Enter password</strong>

<li><strong>Click“SignUp” button</strong>
</li>
</ol>
   </td>
   <td><strong>      PASS</strong>
   </td>
  </tr>
  <tr>
   <td><strong>2</strong>
   </td>
   <td><strong>Sign in</strong>
   </td>
   <td>
<ol>

<li><strong>Enter email</strong>

<li><strong>Enter password</strong>

<li><strong>Click“Sign in” button</strong>
</li>
</ol>
   </td>
   <td><strong>      PASS</strong>
   </td>
  </tr>
  <tr>
   <td><strong>3</strong>
   </td>
   <td><strong>Post media </strong>
   </td>
   <td>
<ol>

<li><strong>Click on plus on profile page</strong>

<li><strong>Enter description</strong>

<li><strong>Upload Image</strong>

<li><strong>Click “Post” button</strong>
</li>
</ol>
   </td>
   <td><strong>        PASS</strong>
   </td>
  </tr>
  <tr>
   <td><strong>4</strong>
   </td>
   <td><strong>Link spotify</strong>
   </td>
   <td>
<ol>

<li><strong>Click Link Spotify button</strong>

<li><strong>Accept terms of use</strong>
</li>
</ol>
   </td>
   <td><strong>        PASS</strong>
   </td>
  </tr>
  <tr>
   <td><strong>5</strong>
   </td>
   <td><strong>Link Location</strong>
   </td>
   <td>
<ol>

<li><strong>Click Link location services</strong>

<li><strong>Enable location in settings</strong>
</li>
</ol>
   </td>
   <td><strong>       PASS</strong>
   </td>
  </tr>
  <tr>
   <td><strong>6</strong>
   </td>
   <td><strong>Change Avatar</strong>
   </td>
   <td>
<ol>

<li><strong>Click on avatar icon</strong>

<li><strong>Upload image </strong>
</li>
</ol>
   </td>
   <td><strong>       PASS</strong>
   </td>
  </tr>
  <tr>
   <td><strong>7</strong>
   </td>
   <td><strong>Search for event</strong>
   </td>
   <td>
<ol>

<li><strong>Click on search bar </strong>

<li><strong>Type request into bar</strong>

<li><strong>View results</strong>
</li>
</ol>
   </td>
   <td><strong>       PASS</strong>
   </td>
  </tr>
</table>


**6.3 Version Control**

**We made use of github for version control and branches. This was used within Android Studio for increased work productivity. We also made use of a staging branch and a user branch for version control. **

**Side Note:**

Github was used throughout project development instead of Gitlab. due to integration issues with Android Studio [https://github.com/drowe4/LiveWire](https://github.com/drowe4/LiveWire). Also project member Eoin Mc Keever was not able to integrate Github with Android Studio due to an issue with his Android Studio account and Github account not linking correctly as a result of this all completed work was sent on and uploaded by one of the other group members.

   </td>
  </tr>
  <tr>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
  </tr>
</table>



<!-- Docs to Markdown version 1.0β18 -->