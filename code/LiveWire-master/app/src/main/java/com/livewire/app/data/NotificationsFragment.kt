package com.livewire.app.data

import android.content.Context
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.firestore.*
import com.livewire.app.R

class NotificationsFragment : Fragment() {

    private var db: FirebaseFirestore = FirebaseFirestore.getInstance()
    private var artistsnames: ArrayList<String> = ArrayList()
    private var locationsnames: ArrayList<String> = ArrayList()
    private var prnames: ArrayList<String> = ArrayList()
    private var sdnames: ArrayList<String> = ArrayList()
    private var stnames: ArrayList<String> = ArrayList()
    private var statnames: ArrayList<String> = ArrayList()
    private var TAG: String = "NotiFragment"
    lateinit var textViewart: TextView
    lateinit var textViewloc: TextView
    lateinit var textViewpr: TextView
    lateinit var textViewsd: TextView
    lateinit var textViewst: TextView
    lateinit var textViewstat: TextView




    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        var view: View = inflater.inflate(R.layout.fragment_notifications, container, false)
        var context:Context? = container?.context
        val uid = FirebaseAuth.getInstance().currentUser!!.uid
        var reco = ArrayList<String>()
        var list = ArrayList<String>()

        db.document("notifications/$uid").addSnapshotListener{ documentSnapshot: DocumentSnapshot?, e: FirebaseFirestoreException? ->
            list = documentSnapshot!!.get("recommendedListings") as ArrayList<String>
            for (li in list){
                reco.add(li)
            }
            Log.println(Log.ASSERT, "reco", reco.toString())
            for (item in reco){
                Log.println(Log.ASSERT, "recoloop","beforeloop")
                db.document("listings/$item").addSnapshotListener{documentSnapshot1: DocumentSnapshot?, e: FirebaseFirestoreException? ->
                    artistsnames.add(documentSnapshot1!!.get("artists").toString())
                    Log.println(Log.ASSERT, "recoloop",artistsnames.size.toString())
                    locationsnames.add("Venue:                                              "+documentSnapshot1.get("locations").toString())
                    prnames.add("Price: "+documentSnapshot1!!.get("pricerange").toString())
                    sdnames.add(documentSnapshot1!!.get("startdate").toString())
                    stnames.add(documentSnapshot1!!.get("starttime").toString())
                    statnames.add(documentSnapshot1!!.get("status").toString())
                }
            }

        }


        //Log.println(Log.ASSERT, "artistssize",artistsnames.size.toString())
        val recyclerView: RecyclerView  = view.findViewById(R.id.listviewnoti)
        val adapter  = RecyclerViewAdapter(artistsnames, locationsnames, prnames, sdnames,stnames,statnames,context!!)

        recyclerView.setLayoutManager(LinearLayoutManager(context))
        Log.println(Log.ASSERT, "initRecyclerView","recycler")
        recyclerView.adapter = adapter


        return view





    }

    override fun onStop() {
        super.onStop()
        artistsnames = ArrayList()
        locationsnames= ArrayList()
        prnames = ArrayList()
        sdnames = ArrayList()
        stnames = ArrayList()
        statnames = ArrayList()

    }
}

