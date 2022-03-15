# Supported Event Types
* The left column of the table below lists the values that you can see in the Halo portal's Events screen. 
The right column lists the equivalent value that you can supply for the type parameter in the List events call.

* For each event type that you pass in the type parameter for your call, you must provide the exact spelling shown(except for capitalization, which does not matter). 
If you pass any other spelling, it is considered an unknown value and the call returns no results.

|Portal Value|API Value|
|-----------|----------|
|**API Key Management**|
|Api key created|api_client_created|
|Api key deleted|api_client_deleted|
|Api secret key viewed|api_client_secret_viewed|
|Api key modified|api_client_updated|
|**Cloud Service Provider Events**|
|Cloud asset configuration rule failed|cloud_asset_configuration_rule_failed|
|CSP account deactivated|csp_account_deactivated|
|CSP account deleted|csp_account_deleted|
|CSP account details modified|csp_account_details_changed|
|CSP account provisioned|csp_account_provisioned|
|CSP account reactivated|csp_account_reactivated|
|CSP account scan schedule changed|csp_account_scan_schedule_changed|
|CSP account scan scheduled|csp_account_scan_scheduled|
|**Configuration Security Management**|
|Configuration policy assigned|sca_policy_assigned|
|Configuration policy created|sca_policy_created|
|Configuration policy deleted|sca_policy_deleted|
|Configuration policy modified|sca_policy_modified|
|Configuration policy unassigned|sca_policy_unassigned|
|Configuration scan terminated|sca_scan_terminated|
|**Connector Events**|
|Connector compromised|image_collector_compromised|
|Connector deactivated|image_collector_deactivated|
|Connector deleted|image_collector_deleted|
|Connector missing|image_collector_missing|
|Connector reactivated|image_collector_reactivated|
|Connector registered|image_collector_registered|
|Connector registration failed|image_collector_registration_failed|
|Connector registration key regenerated|image_collector_registration_key_regenerated|
|Connector modified|image_collector_settings_modified|
|**File Integrity Scanning Management**|
|File integrity baseline|fim_baseline_created|
|File integrity baseline deleted|fim_baseline_deleted|
|File integrity baseline expired|fim_baseline_expired|
|File integrity baseline failed|fim_baseline_failed|
|File integrity baseline invalid|fim_baseline_invalid|
|File integrity policy assigned|fim_policy_assigned|
|File integrity policy created|	fim_policy_created|
|File integrity policy deleted|	fim_policy_deleted|
|File integrity policy modified|	fim_policy_modified|
|File integrity policy unassigned|	fim_policy_unassigned|
|File integrity re-baseline|	fim_re_baseline|
|Automatic file integrity scanning disabled|	fim_scan_disabled|
|Automatic file integrity scanning enabled|	fim_scan_enabled|
|File integrity scan failed|	fim_scan_failed|
|Automatic file integrity scan schedule modified|	fim_scan_modified|
|File integrity scan requested|	fim_scan_requested|
|File integrity scan terminated|	fim_scan_terminated|
|**Firewall Management**|
|Halo firewall policy assigned|	firewall_policy_assigned|
|Halo firewall policy created|	firewall_policy_created|
|Halo firewall policy deleted|	firewall_policy_deleted|
|Halo firewall policy modified|	firewall_policy_modified|
|Halo firewall policy unassigned|	firewall_policy_unassigned|
|Server firewall restore requested|	firewall_restore_requested|
|Network service added|	firewall_service_added|
|Network service deleted|	firewall_service_deleted|
|Network service modified|	firewall_service_modified|
|**GhostPorts**|
|Ghostports session close|	ghostport_close|
|Ghostports login failure|	ghostport_failure|
|Ghostports provisioning|	ghostport_provisioning|
|Ghostports login success|	ghostport_success|
|**Halo Agent Management**|
|Agent restarted|	agent_restarted|
|Agent upgrade failed|	agent_upgrade_failed|
|Agent upgrade succeeded|	agent_upgrade_succeeded|
|Agent upgrade task cancelled|	agent_upgrade_task_cancelled|
|Agent upgrade task completed|	agent_upgrade_task_completed|
|Agent upgrade task scheduled|	agent_upgrade_task_scheduled|
|Automatic server retirement setting modified|	daemon_retirement_timeout_modified|
|Daemon settings modified|	daemon_settings_modified|
|Daemon version changed|	daemon_version_change|
|Agent firewall collection setting modified|	firewall_collection_setting_modified|
|Agent scan time limit modified|	scan_time_limit_modified|
|**Halo Users and Authentication**|
|Halo user activation failed|	activation_link_failed|
|Halo api authentication failure|	api_login_failure|
|Halo api authentication success|	api_login_success|
|Halo authentication settings modified|	authentication_settings_modified|
|Authorized ips modified|	authorized_ips_modified|
|Halo login failure|	halo_login_failure|
|Halo login success|	halo_login_success|
|Halo user deactivated|	halo_user_deactivated|
|Halo user deleted|	halo_user_deleted|
|Halo user invited|	halo_user_invited|
|Halo user account locked|	halo_user_locked|
|Halo logout|	halo_user_logout|
|Halo user modified|	halo_user_modified|
|Halo user reactivated|	halo_user_reactivated|
|Halo user re-invited|	halo_user_reinvited|
|Halo user account unlocked|	halo_user_unlocked|
|Master account linked|	master_account_linked|
|Halo password changed|	password_changed|
|Halo password authentication settings modified|	password_config_changed|
|Halo password recovery request failed|	password_recovery_request_failed|
|Halo password recovery requested|	password_recovery_requested|
|Halo password recovery success|	password_recovery_success|
|Halo session timeout|	session_timeout|
|Halo session timeout modified|	session_timeout_modified|
|Sms phone number configured|	sms_phone_number_configured|
|TOTP configured|	totp_configured|
|Yubikey configured|	yubikey_configured|
|**Image Events**|
|Ci image scan completed|	ci_image_scan_completed|
|Image inspection status changed|	image_inspection_status_changed|
|Image issue resolved|	image_issue_resolved|
|Image security status changed|	image_security_status_changed|
|Image status changed|	image_status_changed|
|Vulnerable software package on image|	vulnerable_software_package_found_on_image|
|**Image Registry Events**|
|Image registry added|	registry_add|
|Image registry changed|	registry_changed|
|Image registry deleted|	registry_deleted|
|Image registry status changed|	registry_status_changed|
|Image repository added|	repository_add|
|Image repository deleted|	repository_delete|
|Image repository modified|	repository_modified|
|**Key Management**|
|Key created|	key_created|
|Key deleted|	key_deleted|
|Key delivery success|	key_delivery_success|
|Key expired|	key_expired|
|Key request success|	key_request_success|
|Key status updated|	key_status_updated|
|Key management policy assigned|	km_policy_assigned|
|Key management policy created|	km_policy_created|
|Key management policy deleted|	km_policy_deleted|
|Key management policy modified|	km_policy_modified|
|Key management policy unassigned|	km_policy_unassigned|
|**Log-Based Intrusion Detection Management**|
|Log-based intrusion detection policy assigned|	lids_policy_assigned|
|Log-based intrusion detection policy created|	lids_policy_created|
|Log-based intrusion detection policy deleted|	lids_policy_deleted|
|Log-based intrusion detection policy modified|	lids_policy_modified|
|Log-based intrusion detection policy unassigned|	lids_policy_unassigned|
|Log-based intrusion detection disabled|	lids_scan_disabled|
|Log-based intrusion detection enabled|	lids_scan_enabled|
|**Server Access Management**|
|Local account activation requested|	local_account_activate_request|
|Local account creation requested|	local_account_create_request|
|Local account deactivation requested|	local_account_deactivate_request|
|Local account modification requested|	local_account_update_request|
|Local account ssh keys update requested|	local_account_update_ssh_keys_request|
|**Server Events**|
|Daemon compromised*|	daemon_compromised*|
|Multiple accounts detected with same uid (linux only)|	duplicate_uid_accounts|
|File integrity change detected|	fim_target_integrity_changed|
|Server ip address changed|	ip_address_changed|
|Log-based intrusion detection rule matched|	lids_rule_failed|
|Multiple root accounts detected (linux only)|	multiple_root_accounts|
|New server|	new_server|
|Configuration rule matched|	sca_rule_failed|
|Local account created|	server_account_created|
|Local account deleted|	server_account_deleted|
|Server deactivated|	server_deactivated|
|Server deleted|	server_deleted|
|Server firewall modified|	server_firewall_modified_locally|
|Server missing|	server_missing|
|Server reactivated|	server_reactivated|
|Server retired|	server_retired|
|Server un-retired|	server_unretired|
|Vulnerable software package found|	vulnerable_software_package_found|
|Server moved to another group|	server_moved|
|**Software Vulnerability Assessment Management**|
|Software vulnerability exception created|	cve_exception_created|
|Software vulnerability exception deleted|	cve_exception_deleted|
|Software vulnerability exception expired|	cve_exception_expired|
|Software vulnerability exception updated|	cve_exception_updated|
|Software vulnerability scan terminated|	svm_scan_terminated|
|**Uncategorized**|
|Agent registration key regenerated|	agent_key_regenerated|
|Container event detected|	container_event_add|
|Container inspection disabled|	container_inspection_disabled|
|Container inspection enabled|	container_inspection_enabled|
|Issue resolved|	issue_resolved|
|Portal audit policy modified|	portal_audit_policy_modified|
|Server account scan requested|	sam_scan_requested|
|Group added|	server_group_added|
|Group deleted|	server_group_deleted|
|Group moved|	server_group_moved|