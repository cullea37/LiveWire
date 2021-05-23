package com.livewire.app.data

import android.app.Activity.RESULT_OK
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.ImageView
import androidx.core.view.isInvisible
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentTransaction
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.FirebaseDatabase
import com.livewire.app.R
import kotlinx.android.synthetic.main.fragment_post.*
import java.net.URI

class MakePost : Fragment() {

    lateinit var imageURI: Uri
    lateinit var imageView: ImageView

    companion object {
        fun newInstance(): HomeFragment {
            return HomeFragment()
        }

    }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        var view: View = inflater.inflate(R.layout.fragment_post, container, false)
        var context: Context? = container?.context
        val button: Button = view.findViewById(R.id.back)
        //val imageView: ImageView = view.findViewById(R.id.image)
        val GALLERY_REQUEST_CODE = 123

        button.setOnClickListener{
            val transaction: FragmentTransaction = fragmentManager!!
                .beginTransaction()
            /*
		 * When this container fragment is created, we fill it with our first
		 * "real" fragment
		 */
            /*
		 * When this container fragment is created, we fill it with our first
		 * "real" fragment
		 */ transaction.replace(R.id.post_frag, ProfileFragment())

            transaction.commit()
            view.visibility = View.GONE
        }

        val imagebtn: Button = view.findViewById(R.id.imagebtn)

        imagebtn.setOnClickListener {
            val intent: Intent = Intent()
            val imageView: ImageView = view.findViewById(R.id.image)
            intent.setType("image/*")
            intent.setAction(Intent.ACTION_GET_CONTENT)
            startActivityForResult(Intent.createChooser(intent, "Pick image"), GALLERY_REQUEST_CODE)

        }

        val postbtn: Button = view.findViewById(R.id.postbtn)
        postbtn.setOnClickListener {

        }

        return view


    }
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == RESULT_OK){
            imageURI = data!!.data!!
            imageView.setImageURI(imageURI)
        }

    }


}