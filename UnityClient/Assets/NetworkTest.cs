using System.Collections;
using System.Collections.Generic;
using System.Threading.Tasks;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Networking;

public class NetworkTest : MonoBehaviour
{
    string Address = "http://192.168.0.35:9022/GetWebPage";
    void Start()
    {
        SendMessageToServer();
    }
    void SendMessageToServer()
    {
        StartCoroutine(SendMessageToServerProcess());
    }
    IEnumerator SendMessageToServerProcess()
    {
        var form = new WWWForm();
        form.AddField("id_username", "a");
        form.AddField("id_password", "b");
        UnityWebRequest www = UnityWebRequest.Post(Address, form);
        www.redirectLimit = 10;
        yield return www.SendWebRequest();
        if (www.result == UnityWebRequest.Result.ConnectionError || www.result == UnityWebRequest.Result.ProtocolError)
        {
            Debug.Log(www.error);
        }
        else
        {
            Debug.Log(www.downloadHandler.text);
        }
        www.Dispose();
    }
}