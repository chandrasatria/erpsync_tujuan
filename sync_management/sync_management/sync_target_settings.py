# -*- coding: utf-8 -*-
# Copyright (c) 2015, erpx and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import json

class SyncServerSettings(Document):
	pass
@frappe.whitelist()
def switch_name_doc(self, method):
	frappe.db.sql(""" UPDATE `tab{} Item` ol JOIN `tab{} Item` nu USING (NAME) 
		SET nu.name = ol.tampungan_awal, nu.tampungan_awal = ol.name WHERE ol.parent = "{}" """.format(self.doctype, self.doctype, self.name))
	frappe.db.commit()
	frappe.db.close()
