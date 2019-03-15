Title: New parameter "tags" released
Date: 2019-03-15
Slug: tags-with-xoxzo-api
Lang: en
Tags: xoxzo; new release; 2019; tags;
Author: Iqbal Abdullah
Summary: You can now categorize your API calls with the tags parameter

One of the functionality requests that we get concerns the categorization of API calls.

We have released a new functionality which allows you to do just that: Now you can
categorize your API calls by adding an optional **tags** parameter to your API calls.
You can even attach multiple tags to a single API call:

Example:


These tags data will be attached to your SMS and Voice API calls that you make,
and can be retrieved via the Check SMS Status API and the Checking Call Status
API respectively.

Example:


You can use the tags data to categorize your usage of our API, for example,
using different tags for different marketing campaigns or block of customers to
differentiate between them and different messaging that you use.

In the future, we plan to make it easier for you to visualize how and how
effective the different types of your messages and calls are, using these tags data.
