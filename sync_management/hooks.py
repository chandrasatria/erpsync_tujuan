# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sync_management"
app_title = "Sync Management"
app_publisher = "ERPX"
app_description = "Sync document from this server to another"
app_icon = "octicon octicon-book"
app_color = "#589494"
app_email = "erpx@mail.com"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------
fixtures = ["Custom Field",{"doctype":"DocType","filters":{"module":["=","Sync Management"]}  }]
# include js, css files in header of desk.html
# app_include_css = "/assets/sync_management/css/sync_management.css"
# app_include_js = "/assets/sync_management/js/sync_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/sync_management/css/sync_management.css"
# web_include_js = "/assets/sync_management/js/sync_management.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "sync_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sync_management.install.before_install"
# after_install = "sync_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sync_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Order": {
		"on_submit": "sync_management.sync_management.sync_target_settings.switch_name_doc",
		"autoname" : "sync_management.sync_management.sync_target_settings.sync_autoname",
	},
	"Delivery Note": {
		"on_submit": "sync_management.sync_management.sync_target_settings.switch_name_doc",
		"autoname" : "sync_management.sync_management.sync_target_settings.sync_autoname",
	},
	"Sales Invoice": {
		"on_submit": "sync_management.sync_management.sync_target_settings.switch_name_doc",
		"autoname" : "sync_management.sync_management.sync_target_settings.sync_autoname",
	},
	"Material Request": {
		"on_submit": "sync_management.sync_management.sync_target_settings.switch_name_doc",
		"autoname" : "sync_management.sync_management.sync_target_settings.sync_autoname",
	},
	"Purchase Order": {
		"on_submit": "sync_management.sync_management.sync_target_settings.switch_name_doc",
		"autoname" : "sync_management.sync_management.sync_target_settings.sync_autoname",
	},
	"Purchase Receipt": {
		"on_submit": "sync_management.sync_management.sync_target_settings.switch_name_doc",
		"autoname" : "sync_management.sync_management.sync_target_settings.sync_autoname",
	},
	"Purchase Invoice": {
		"on_submit": "sync_management.sync_management.sync_target_settings.switch_name_doc",
		"autoname" : "sync_management.sync_management.sync_target_settings.sync_autoname",
	},
	"Stock Entry": {
		"autoname" : "sync_management.sync_management.sync_target_settings.sync_autoname",
	},
	"Production Order": {
		"autoname" : "sync_management.sync_management.sync_target_settings.sync_autoname",
	},
	"Payment Entry": {
		"autoname" : "sync_management.sync_management.sync_target_settings.sync_autoname",
	},
	"Journal Entry": {
		"autoname" : "sync_management.sync_management.sync_target_settings.sync_autoname",
	},
	"Stock Reconciliation": {
		"autoname" : "sync_management.sync_management.sync_target_settings.sync_autoname",
	},
	"Landed Cost Voucher": {
		"autoname" : "sync_management.sync_management.sync_target_settings.sync_autoname",
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sync_management.tasks.all"
# 	],
# 	"daily": [
# 		"sync_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"sync_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sync_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sync_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sync_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sync_management.event.get_events"
# }

