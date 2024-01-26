<template>
  <q-page>
    <div>
      <h2>MuPIF DB</h2>
      <h3>Visualization Tool</h3>
    </div>

    <q-btn color="primary" @click="onClickLoadDB"> Load database </q-btn>
    <q-btn color="primary" @click="active_DB_log = !active_DB_log"
      >Hide/Show DB data</q-btn
    >
    <q-banner class="bg-secondary text-white">
      <table></table>
      <b>DB state: {{ DBstate }}</b>
      <br />
      <b>DB name: {{ DBname }}</b>
      <br />
      <b>DB URL: {{ DBurl }}</b>
      <br />
      <b>DB_obj_ID: {{ DB_obj_ID }}</b>
    </q-banner>
    <h5 v-if="active_DB_log">DB data: {{ textJSON }}</h5>
    <q-input
      v-model="maxDepth"
      label="Insert maximal graph depth"
      type="number"
    ></q-input>
    <!-- <q-btn label="Refresh" color="primary" @click="refreshGraph()"></q-btn> -->
    <q-btn color="primary" @click="initGraph()">Create graph</q-btn>
    <!-- <button @click="initGraph()">Create graph</button> -->
    <!-- <button @click="showGraph = !showGraph">Hide/Show Graph</button> -->
    <div>
      <q-toolbar>
        <q-btn @click="collapse_selected_elements()" label="Collapse All" />
        <q-btn @click="expand_selected_elements()" label="Expand All" />
        <!-- <q-btn -->
        <!-- @click="console.log('NOT IMPLEMENTED')"
          label="Collapse Layer"
        /> -->
        <q-btn
          @click="expand_a_layer_of_selected_elements()"
          label="Expand Layer"
        />
        <q-btn @click="remove_selected_elements()" label="Remove Selected" />
      </q-toolbar>
    </div>
    <div id="cy" style="width: 100%; height: 400px">
      <!-- Add more buttons as needed -->
    </div>
    <!-- <div id="maxDepth" style="width: 100%; height: 400px"></div> -->
    <q-banner class="bg-secondary text-white">
      <div class="q-ma-md">
        <q-scroll-area style="height: 200px; max-width: 300px">
          <h6>Selected node</h6>
          <div class="q-pa-md">
            <q-table
              flat
              bordered
              title="Treats"
              :rows="TableRows"
              :columns="TableColumns"
              row-key="name"
              selection="single"
              v-model:selected="selected"
            />

            <div class="q-mt-md">Selected: {{ JSON.stringify(selected) }}</div>
          </div>
          <!-- <div v-for="n in 100" :key="n" class="q-py-xs">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.
          </div> -->
        </q-scroll-area>
      </div>
    </q-banner>
  </q-page>

  <q-page class="flex flex-center">
    <!-- <img
          alt="Quasar logo"
          src="~assets/quasar-logo-vertical.svg"
          style="width: 200px; height: 200px"
    > -->
  </q-page>
</template>

<script>
// TODO  - fix the maximal depth limitation to behave only as initial restriction or make two depth limitation (initial printing limitation and total loading limitation)
// TODO -* show the properties of selected nodes in table below the visualization window

import { defineComponent } from "vue";
import cytoscape from "cytoscape";
import dagre from "cytoscape-dagre";
import cola from "cytoscape-cola";
import axios from "axios";
import expandCollapse from "cytoscape-expand-collapse";
import { data } from "autoprefixer";
import { stringify } from "postcss";
// import { json } from "stream/consumers";
try {
  cytoscape.use(cola);
  cytoscape.use(expandCollapse);
  cytoscape.use(cola);
} catch (err) {
  console.log(err);
}

export default defineComponent({
  data() {
    return {
      DBstate: "No DB is loadeed.",
      DBname: null,
      DBurl: null,
      DB_obj_ID: null,
      textJSON: null,
      fJSON: null,
      active_DB_log: false,
      showGraph: true,
      TableColumns: ["entity"],
      maxDepth: 3,
      GraphData: null,
      cyGraph: null,
      name: "IndexPage",
    };
  },
  methods: {
    hide_parents() {
      console.log("NOT IMPLEMENTED");
      // this.cyGraph.$(":selected").forEach(function (Node) {
      //   Node.ancestors().style({
      //     visibility: "hidden",
      //   });
      // });
    },
    show_parents() {
      console.log("NOT IMPLEMENTED");
      // this.cyGraph.$(":selected").forEach(function (Node) {
      //   Node.ancestors().style({
      //     visibility: "visible",
      //   });
      // });
    },
    remove_selected_elements() {
      const confirmation = window.confirm(
        "Are you sure you want to remove selected elements, they will be irreversibly deleted from the view? \n\n(Only the visualization will be affected, your database remains unchanged.)"
      );
      if (confirmation) {
        this.cyGraph.$(":selected").remove();
      }
    },
    collapse_selected_elements() {
      this.cyGraph.$(":selected").forEach(function (parentNode) {
        parentNode.children().style({
          display: "none",
        });
      });
    },
    expand_selected_elements() {
      this.cyGraph.$(":selected").forEach(function (parentNode) {
        parentNode.children().style({
          display: "element",
        });
      });
    },
    expand_a_layer_of_selected_elements() {
      this.cyGraph.$(":selected").forEach(function (parentNode) {
        parentNode.children().style({
          display: "element",
        });
        parentNode.children().forEach(function (parentNode) {
          parentNode.children().style({
            display: "none",
          });
        });
      });
    },
    hide_the_last_layer_recursively(node) {
      // not implemented
      // if children is none or are hidden, hide layer and break
      console.log(node);
      console.log(this.cyGraph.expandCollapse.isCollapsile(node));
      if (node.children().style().display == "none") {
        return true;
      }
      // =hide_the_last_layer_recursively(node.children());
    },
    collapse_a_layer_of_selected_elements() {
      // this.ceapi.collapseRecursively(this.cyGraph.$(":slected"),);
      // console.log(this.cyGraph.$(":selected"));
      // this.cyGraph.$(":selected").forEach(function (parentNode) {
      //   parentNode.children().last().style({
      //     display: "none",
      //   });
      // });
      this.cyGraph.$(":selected").forEach(function (parentNode) {
        hide_the_last_layer_recursively;
      });
    },
    post_DB_API(subName) {
      try {
        const sendData = this.textJSON;
        this.myID = axios.post(this.DBurl + "/" + this.DBname + "/" + subName, {
          sendData,
        });
        console.log(responseData);
      } catch (err) {
        console.log(err);
      }
    },
    async get_DB_API() {
      // try {
      //   const responseData = await axios.get(
      //     this.DBurl + "/" + this.DBname + "/" + ID
      //   );
      //   console.log(responseData);
      // } catch (err) {
      //   console.log(err);
      // }
    },

    onClickLoadDB() {
      // this.active_DB_log = true;
      this.DBstate = "Not implemented function - a test file loaded instead.";
      this.DBname = prompt("Enter DB name", "dms0");
      this.DBurl = prompt("Enter DB URL", "http://127.0.0.1:5000/");
      this.DB_obj_ID = prompt("Enter DB obj ID", null);

      this.getDBtest_JSON();
      this.subName = "BeamState";
      this.DB_obj_ID = this.post_DB_API(this.subName);
      console.log(this.DB_obj_ID);
    },
    refreshGraph() {
      this.maxDepth = document.getElementById("myDepth").value;
      console.log(this.maxDepth);
      this.initGraph();
    },
    getGraphDataFromJSON() {
      this.GraphData = {
        nodes: [],
        edges: [],
      };

      try {
        this.GraphData.nodes.push({ data: { id: "data", label: "data" } });
        this.diveDeeperIntoJSON(this.fJSON["data"], "data", 1);
      } catch (error) {
        console.log(error);
      }
    },
    diveDeeperIntoJSON(parentObject, parentKey, level) {
      if (level > this.maxDepth) {
        return;
      }
      console.log(level);
      for (let [key, value] of Object.entries(parentObject)) {
        this.GraphData.nodes.push({
          data: { id: key, parent: parentKey, label: key },
          // data: { id: key, label: key },
        });
        this.GraphData.edges.push({
          data: {
            source: parentKey,
            target: key,
            label: key + "/" + parentKey,
          },
        });

        if (
          Object.keys(value).length >= 2 &&
          typeof value === "object" &&
          !Array.isArray(value) &&
          !null
        ) {
          this.diveDeeperIntoJSON(value, key, (level += 1));
        }
      }
    },
    initGraph() {
      try {
        const graphDataTest = {
          nodes: [
            {
              data: {
                id: "xx1",
                label: "node 1",
              },
            },
            { data: { id: "xx2", label: "node 2" } },
            { data: { id: "x21", label: "node 2a" } },
            { data: { id: "x22", label: "node 2b" } },
            { data: { id: "x23", label: "node 2c" } },
          ],
          edges: [
            { data: { source: "xx1", target: "xx2", label: "Edge 1/2" } },
            { data: { source: "xx2", target: "x21", label: "Edge 2/2a" } },
            { data: { source: "xx2", target: "x22", label: "Edge 2/2b" } },
            { data: { source: "xx1", target: "x22", label: "Edge 1/2b" } },
            { data: { source: "xx2", target: "x23", label: "Edge 2/2c" } },
          ],
        };
        this.getGraphDataFromJSON();
        this.cyGraph = cytoscape({
          container: document.getElementById("cy"),
          elements: this.GraphData, //graphDataTest,
          style: [
            {
              selector: "node",
              style: {
                "background-color": "#183896",
                "background-opacity": 0.5,
                label: "data(label)",
                // shape: "circle",
              },
            },
            {
              selector: "edge",
              style: {
                width: 2,
                "line-color": "#ccc",
                "target-arrow-color": "#ccc",
                "target-arrow-shape": "triangle",
              },
            },
          ],
        });
        var layout = this.cyGraph.layout({
          // name: "cola",
          // // name: "avsdf",
          name: "breadthfirst",
          // name: "cola",
          // directed: true,
          // circle: true,
          // roots: "#data",
          // // directed: true,
          // padding: 18,
        });
        // var layout = cyGraph.layout({
        //   // name: "dagre",
        //   // // name: "avsdf",
        //   // name: "cola",
        //   name: "breadthfirst",
        //   // directed: true,
        //   // circle: true,
        //   // roots: "#data",
        //   // // directed: true,
        //   avoidOverlap: false,
        //   padding: 40,
        // });
        layout.run();
      } catch (error) {
        console.log(error);
        cy;
      }
    },
    async getDBtest_JSON() {
      try {
        const jsonFile = await axios.get("./testDB.json");
        // console.log(jsonFile);
        this.textJSON = JSON.stringify(jsonFile);
        this.fJSON = JSON.parse(this.textJSON);
      } catch (error) {
        console.error(error);
        this.textJSON = "An error occurred.";
      }
    },
  },
});
</script>
