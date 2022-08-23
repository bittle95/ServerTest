using System.Collections;
using System.Collections.Generic;
using System.Threading.Tasks;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Networking;
using Newtonsoft.Json;

public class NetworkTest : MonoBehaviour
{
    string MainAddress = "http://192.168.0.2:9021";
    void Start()
    {
        SendMessageToServer();
    }
    void SendMessageToServer()
    {
        //StartCoroutine(SendMessageToServerProcess());
        StartCoroutine(GetMessageProcess());
    }
    IEnumerator GetMessageProcess()
    {
        var form = new WWWForm();
        UnityWebRequest www = UnityWebRequest.Get(MainAddress + "/PrintWebPage");
        www.redirectLimit = 10;
        yield return www.SendWebRequest();
        if (www.result == UnityWebRequest.Result.ConnectionError || www.result == UnityWebRequest.Result.ProtocolError)
        {
            Debug.Log(www.error);
        }
        else
        {
            //Debug.Log(www.downloadHandler.text); //이걸로 찍는다
            switch (www.downloadHandler.text)
            {
                case "content1":
                    print(1);
                    break;
                case "content2":
                    print(2);
                    break;
                case "content3":
                    print(3);
                    break;
            }
        }

        www.Dispose();
    }
    IEnumerator SendMessageToServerProcess()
    {
        var form = new WWWForm();
        form.AddField("patient_id", "patient_id");
        form.AddField("patient_stride", "patient_stride");
        form.AddField("patient_width", "발너비");
        form.AddField("overlapping_area", "교차영역");
        form.AddField("foot_size", "발크기");
        form.AddField("chk_info", "f");
        UnityWebRequest www = UnityWebRequest.Post(MainAddress + "/PrintWebPage", form);
        www.redirectLimit = 10;
        yield return www.SendWebRequest();
        if (www.result == UnityWebRequest.Result.ConnectionError || www.result == UnityWebRequest.Result.ProtocolError)
        {
            Debug.Log(www.error);
        }
        else
        {
            Debug.Log(www.downloadHandler.text); //이걸로 찍는다
        }
        www.Dispose();
    }
}