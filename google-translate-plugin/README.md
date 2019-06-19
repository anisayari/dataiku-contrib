# Google Translate connector

## Plugin information

This plugin provides a way to interact with the Google Cloud Translation API  in order to translate your text from any language,
improving text analyses. You can now scrap text from any website and use collected data into your analyses.

It exposes on main API:

* **Google Translate API**: Translation offers the ability to quickly translate between languages, using the best model for your content needs. 
You can build custom models using AutoML Translation or leverage Google’s pre-trained models using Translation API.
[Read the documentation](https://cloud.google.com/translate/docs/apis) for more information. 

## How to set-up

* Install the plugin in Dataiku DSS. The plugin requires the installation of a code env.
* Get a `Service account` from the Google API Console with the `Cloud Translation API` enabled. Export the credentials as a `JSON` file.


## How to get the JSON Service Account

In order to use the plugin, you will need service account's credentials exported in a JSON file with the Sheets API enabled. 
To generate this JSON, do the following:

	* Open the Service accounts page in the Google API Console 
	https://console.developers.google.com/projectselector2/iam-admin/serviceaccounts?pli=1&supportedpurview=project&project&folder&organizationId). 
	Create a new project (or select an existing one).

	* Click Create service account. Choose a name for the service account, go through the process, and click Create key and choose JSON
	for the key type. Your browser will download the key. Click Done to finish the creation of the service account.

	* Open the JSON key in a text editor and copy-paste the full content of the file in the dataset settings.

	* Open the Cloud Translation API 
	(https://console.developers.google.com/apis/library/translate.googleapis.com?q=transl&id=c22f20ba-6a29-40ae-9084-8bc264a97fc2&project=dataiku-translate-plugin-666)
	the API Library section of the Google API Console. Make sure you are using the same project than previously. Click on Enable API.
	
	* Done. You can now configure your dataset in Dataiku DSS. Note that the service account can be reused for several datasets/sheets.


## Need help?

Ask your question on [answers.dataiku.com](https://answers.dataiku.com). Or, [open an issue](https://github.com/dataiku/dataiku-contrib/issues).