<template id="proposal_dashboard">
    <div class="container" id="paymentDash">
    <div class="row">
        <div class="col-sm-12">
            <div class="panel panel-default">
                <div class="panel-heading">
                    <h3 class="panel-title">Admission Fees <small v-if="is_external">View existing admission bookings</small>
                        <a :href="'#'+pBody" data-toggle="collapse"  data-parent="#userInfo" expanded="true" :aria-controls="pBody">
                            <span class="glyphicon glyphicon-chevron-up pull-right "></span>
                        </a>
                    </h3>
                </div>
                <div class="panel-body collapse in" :id="pBody">
                    <div class="row">
                        <div class="col-md-3">
                            <div class="form-group">
                                <label for="">Park</label>
                                <select class="form-control" v-model="filterProposalPark">
                                    <option value="All">All</option>
                                    <option v-for="p in proposal_parks" :value="p.id">{{p.name}}</option>
                                </select>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="form-group">
                                <label for="">Status</label>
                                <select class="form-control" v-model="filterProposalStatus">
                                    <option value="All">All</option>
                                    <option v-for="s in payment_status" :value="s.value">{{s.name}}</option>
                                </select>
                            </div>
                        </div>
                        <div v-if="is_external" class="col-md-3">
                            <div class="form-group">
                                <router-link  style="margin-top:25px;" class="btn btn-primary pull-right" :to="{ name: 'payment_order'  }">Make Payment</router-link>
                            </div>
                        </div>

                    </div>
                    <div class="row">
                        <div class="col-md-3">
                            <div class="form-group">
                                <label for="">Arrival From</label>
                                <div class="input-group date" ref="proposalDateFromPicker">
                                    <input type="text" class="form-control" placeholder="DD/MM/YYYY" v-model="filterProposalLodgedFrom">
                                    <span class="input-group-addon">
                                        <span class="glyphicon glyphicon-calendar"></span>
                                    </span>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="form-group">
                                <label for="">Arrival To</label>
                                <div class="input-group date" ref="proposalDateToPicker">
                                    <input type="text" class="form-control" placeholder="DD/MM/YYYY" v-model="filterProposalLodgedTo">
                                    <span class="input-group-addon">
                                        <span class="glyphicon glyphicon-calendar"></span>
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-lg-12" style="margin-top:25px;">
                            <datatable ref="proposal_datatable" :id="datatable_id" :dtOptions="proposal_options" :dtHeaders="proposal_headers"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>


    </div>
    </div>
</template>
<script>
import datatable from '@/utils/vue/datatable.vue'
import Vue from 'vue'

import {
    api_endpoints,
    helpers
}from '@/utils/hooks'
export default {
    name: 'ProposalTableDash',
    props: {
        level:{
            type: String,
            required: true,
            validator:function(val) {
                let options = ['internal','referral','external'];
                return options.indexOf(val) != -1 ? true: false;
            }
        },
        url:{
            type: String,
            required: true
        }
    },
    components:{
        datatable,
    },
    data() {
        let vm = this;
        return {
            pBody: 'pBody' + vm._uid,
            datatable_id: 'proposal-datatable-'+vm._uid,
            //Profile to check if user has access to process Proposal
            profile: {},
            // Filters for Proposals
            filterProposalPark: 'All',
            filterProposalStatus: 'All',
            filterProposalLodgedFrom: '',
            filterProposalLodgedTo: '',
            filterProposalSubmitter: 'All',
            dateFormat: 'DD/MM/YYYY',
            datepickerOptions:{
                format: 'DD/MM/YYYY',
                showClear:true,
                useCurrent:false,
                keepInvalid:true,
                allowInputToggle:true
            },
            payment_status:[
                {name:'Paid', value:'paid'},
                {name:'Over Paid', value:'over_paid'},
                {name:'Partially Paid', value:'partially_paid'},
                {name:'Unpaid', value:'unpaid'}
            ],
            proposal_submitters: [],
            proposal_parks: [],
            proposal_headers:[
                " Number","Licence","Holder","Status","Arrival","Park","Invoice/Confirmation","Action",
            ],
            proposal_options:{
                language: {
                    processing: "<i class='fa fa-4x fa-spinner fa-spin'></i>"
                },
                responsive: true,
                serverSide: true,
                lengthMenu: [ [10, 25, 50, 100, -1], [10, 25, 50, 100, "All"] ],
                ajax: {
                    //"url": vm.url,
                    //"url": '/api/booking_paginated/bookings_external/?format=datatables',
                    "url": api_endpoints.booking_paginated_internal,
                    "dataSrc": 'data',

                    // adding extra GET params for Custom filtering
                    "data": function ( d ) {
                        d.park = vm.filterProposalPark != 'All' && vm.filterProposalPark != null ? vm.filterProposalPark : '';
                        d.payment_status = vm.filterProposalStatus != 'All' && vm.filterProposalStatus != null ? vm.filterProposalStatus : '';
                        d.date_from = vm.filterProposalLodgedFrom != '' && vm.filterProposalLodgedFrom != null ? moment(vm.filterProposalLodgedFrom, 'DD/MM/YYYY').format('YYYY-MM-DD'): '';
                        d.date_to = vm.filterProposalLodgedTo != '' && vm.filterProposalLodgedTo != null ? moment(vm.filterProposalLodgedTo, 'DD/MM/YYYY').format('YYYY-MM-DD'): '';
                    }

                },
                dom: 'lBfrtip',
                buttons:[
                'excel', 'csv', ],
                columns: [
                    {
                        data: "admission_number",
                        name: "admission_number"
                    },
                    {
                        data: "approval_number",
                        name: "proposal__approval__lodgement_number"
                    },
                    {
                        data: "applicant",
                        name: "proposal__approval__org_applicant__organisation__name, proposal__approval__proxy_applicant__email, proposal__approval__proxy_applicant__first_name, proposal__approval__proxy_applicant__last_name"
                    },
                    {
                        data: "payment_status",
                        name: "payment_status",
                        searchable: false,
                        orderable: false
                    },
                    {
                        data: "park_bookings",
                        mRender:function (data,type,full) {
                            let arrival_dates = '';
                            _.forEach(data, function (park) {
                                arrival_dates += (park.arrival != '' && park.arrival != null ? moment(park.arrival).format(vm.dateFormat): '') + '<br>';
                                //arrival_dates += arrival_dates + '<br>'
                            });
                            return arrival_dates;
                        },
                        searchable: false,
                        orderable: true
                    },
                    {
                        data: "park_bookings",
                        mRender:function (data,type,full) {
                            let parks = '';
                            _.forEach(data, function (item) {
                                parks += item.park + '<br>';
                            });
                            return parks;
                        },
                        //name: "park__id, park__name"
                        name: "park_bookings__park__name"

                    },

                    {
                        data: '',
                        mRender:function (data,type,full) {
                            let links = '';
                            if (full.payment_status=='paid'){
                                links +=  `<a href='/cols/payments/invoice-pdf/${full.invoice_reference}' target='_blank'><i style='color:red;' class='fa fa-file-pdf-o'></i></a> &nbsp`;
                                links +=  `<a href='/cols/payments/confirmation-pdf/${full.invoice_reference}' target='_blank'><i style='color:red;' class='fa fa-file-pdf-o'></i></a><br/>`;
                            }
                            return links;
                        },
                        name: '',
                        searchable: false,
                        orderable: false
                    },
                    {
                        data: "",
                        mRender:function (data,type,full) {
                            let links = '';
                            if (full.payment_status=='paid'){
                                links +=  `<a href='/ledger/payments/invoice/payment?invoice=${full.invoice_reference}' target='_blank'>View Payment</a><br/>`;
                            }
                            return links;
                        },
                        name: '',
                        searchable: false,
                        orderable: false
                    }

                ],
                processing: true,
                /*
                initComplete: function () {
                    // Grab Status from the data in the table
                    var statusColumn = vm.$refs.proposal_datatable.vmDataTable.columns(5);
                    statusColumn.data().unique().sort().each( function ( d, j ) {
                        let statusTitles = [];
                        $.each(d,(index,a) => {
                            a != null && statusTitles.indexOf(a) < 0 ? statusTitles.push(a): '';
                        })
                        vm.approval_status = statusTitles;
                    });
                    // Fix the table rendering columns
                    vm.$refs.proposal_datatable.vmDataTable.columns.adjust().responsive.recalc();
                }
                */
            }
        }
    },
    watch:{
        filterProposalSubmitter: function(){
            //this.$refs.proposal_datatable.vmDataTable.draw();
            let vm = this;
            if (vm.filterProposalSubmitter!= 'All') {
                vm.$refs.proposal_datatable.vmDataTable.columns(2).search(vm.filterProposalSubmitter).draw();
            } else {
                vm.$refs.proposal_datatable.vmDataTable.columns(2).search('').draw();
            }
        },
        filterProposalStatus: function() {
            let vm = this;
            if (vm.filterProposalStatus!= 'All') {
                vm.$refs.proposal_datatable.vmDataTable.columns(3).search(vm.filterProposalStatus).draw();
            } else {
                vm.$refs.proposal_datatable.vmDataTable.columns(3).search('').draw();
            }
        },
        filterProposalPark: function() {
            let vm = this;
            vm.$refs.proposal_datatable.vmDataTable.columns(5).search('').draw();
        },

        filterProposalLodgedFrom: function(){
            this.$refs.proposal_datatable.vmDataTable.draw();
        },
        filterProposalLodgedTo: function(){
            this.$refs.proposal_datatable.vmDataTable.draw();
        }
    },
    computed: {
        status: function(){
            //return this.is_external ? this.external_status : this.internal_status;
            return [];
        },
        is_external: function(){
            return this.level == 'external';
        },
        is_internal: function(){
            return this.level == 'internal';
        },
    },
    methods:{
        fetchFilterLists: function(){
            let vm = this;

            vm.$http.get(api_endpoints.filter_list_approvals).then((response) => {
                vm.proposal_submitters = response.body.submitters;
                //vm.approval_status = response.body.approval_status_choices;
            },(error) => {
                console.log(error);
            })
            
            vm.$http.get(api_endpoints.filter_list_parks).then((response) => {
                vm.proposal_parks = response.body;
            },(error) => {
                console.log(error);
            })

            //console.log(vm.regions);
        },

        addEventListeners: function(){
            let vm = this;
            // Initialise Proposal Date Filters
            $(vm.$refs.proposalDateToPicker).datetimepicker(vm.datepickerOptions);
            $(vm.$refs.proposalDateToPicker).on('dp.change', function(e){
                if ($(vm.$refs.proposalDateToPicker).data('DateTimePicker').date()) {
                    vm.filterProposalLodgedTo =  e.date.format('DD/MM/YYYY');
                }
                else if ($(vm.$refs.proposalDateToPicker).data('date') === "") {
                    vm.filterProposaLodgedTo = "";
                }
             });
            $(vm.$refs.proposalDateFromPicker).datetimepicker(vm.datepickerOptions);
            $(vm.$refs.proposalDateFromPicker).on('dp.change',function (e) {
                if ($(vm.$refs.proposalDateFromPicker).data('DateTimePicker').date()) {
                    vm.filterProposalLodgedFrom = e.date.format('DD/MM/YYYY');
                    $(vm.$refs.proposalDateToPicker).data("DateTimePicker").minDate(e.date);
                }
                else if ($(vm.$refs.proposalDateFromPicker).data('date') === "") {
                    vm.filterProposalLodgedFrom = "";
                }
            });

            // End Proposal Date Filters
            // Internal Reissue listener
            vm.$refs.proposal_datatable.vmDataTable.on('click', 'a[data-reissue-approval]', function(e) {
                e.preventDefault();
                var id = $(this).attr('data-reissue-approval');
                vm.reissueApproval(id);
            });

            // Internal Extend listener
            vm.$refs.proposal_datatable.vmDataTable.on('click', 'a[data-extend-approval]', function(e) {
                e.preventDefault();
                var id = $(this).attr('data-extend-approval');
                vm.extendApproval(id);
            });


            //Internal Cancel listener
            vm.$refs.proposal_datatable.vmDataTable.on('click', 'a[data-cancel-approval]', function(e) {
                e.preventDefault();
                var id = $(this).attr('data-cancel-approval');
                vm.cancelApproval(id);
            });

            //Internal Suspend listener
            vm.$refs.proposal_datatable.vmDataTable.on('click', 'a[data-suspend-approval]', function(e) {
                e.preventDefault();
                var id = $(this).attr('data-suspend-approval');
                vm.suspendApproval(id);
            });

            // Internal Reinstate listener
            vm.$refs.proposal_datatable.vmDataTable.on('click', 'a[data-reinstate-approval]', function(e) {
                e.preventDefault();
                var id = $(this).attr('data-reinstate-approval');
                vm.reinstateApproval(id);
            });

            //Internal/ External Surrender listener
            vm.$refs.proposal_datatable.vmDataTable.on('click', 'a[data-surrender-approval]', function(e) {
                e.preventDefault();
                var id = $(this).attr('data-surrender-approval');
                vm.surrenderApproval(id);
            });

            // External renewal listener
            vm.$refs.proposal_datatable.vmDataTable.on('click', 'a[data-renew-approval]', function(e) {
                e.preventDefault();
                var id = $(this).attr('data-renew-approval');
                vm.renewApproval(id);
            });

            // External amend listener
            vm.$refs.proposal_datatable.vmDataTable.on('click', 'a[data-amend-approval]', function(e) {
                e.preventDefault();
                var id = $(this).attr('data-amend-approval');
                vm.amendApproval(id);
            });

        },
        initialiseSearch:function(){
            this.dateSearch();
        },
        submitterSearch:function(){
            let vm = this;
            vm.$refs.proposal_datatable.table.dataTableExt.afnFiltering.push(
                function(settings,data,dataIndex,original){
                    let filtered_submitter = vm.filterProposalSubmitter;
                    if (filtered_submitter == 'All'){ return true; } 
                    return filtered_submitter == original.submitter.email;
                }
            );
        },
        dateSearch:function(){
            let vm = this;
            vm.$refs.proposal_datatable.table.dataTableExt.afnFiltering.push(
                function(settings,data,dataIndex,original){
                    let from = vm.filterProposalLodgedFrom;
                    let to = vm.filterProposalLodgedTo;
                    let val = original.expiry_date;

                    if ( from == '' && to == ''){
                        return true;
                    }
                    else if (from != '' && to != ''){
                        return val != null && val != '' ? moment().range(moment(from,vm.dateFormat),moment(to,vm.dateFormat)).contains(moment(val)) :false;
                    }
                    else if(from == '' && to != ''){
                        if (val != null && val != ''){
                            return moment(to,vm.dateFormat).diff(moment(val)) >= 0 ? true : false;
                        }
                        else{
                            return false;
                        }
                    }
                    else if (to == '' && from != ''){
                        if (val != null && val != ''){
                            return moment(val).diff(moment(from,vm.dateFormat)) >= 0 ? true : false;
                        }
                        else{
                            return false;
                        }
                    } 
                    else{
                        return false;
                    }
                }
            );
        },

        fetchProfile: function(){
            let vm = this;
            Vue.http.get(api_endpoints.profile).then((response) => {
                vm.profile = response.body
            },(error) => {
                console.log(error);
            })
        },

        refreshFromResponse: function(){
            this.$refs.proposal_datatable.vmDataTable.ajax.reload();
        },

    },
    mounted: function(){
        this.fetchFilterLists();
        this.fetchProfile();
        let vm = this;
        $( 'a[data-toggle="collapse"]' ).on( 'click', function () {
            var chev = $( this ).children()[ 0 ];
            window.setTimeout( function () {
                $( chev ).toggleClass( "glyphicon-chevron-down glyphicon-chevron-up" );
            }, 100 );
        });
        this.$nextTick(() => {
            vm.addEventListeners();
            vm.initialiseSearch();
        });
    }
}
</script>
<style scoped>
</style>
